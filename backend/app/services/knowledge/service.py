import json
import logging
import os
import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.models.source import EvalRun, Source
from app.schemas.knowledge import (
    EvalRunResult,
    KnowledgeIngestRequest,
    SearchQuery,
    SearchResponse,
    SourceResponse,
)
from app.services.knowledge.ingestion.chunker import HeadingAwareChunker
from app.services.knowledge.interfaces.embedder import BaseEmbedder
from app.services.knowledge.interfaces.reranker import BaseReranker
from app.services.knowledge.interfaces.vector_store import BaseVectorStore
from app.services.knowledge.providers.hybrid_embedder import HybridEmbedder
from app.services.knowledge.providers.qdrant_store import QdrantVectorStore
from app.services.knowledge.providers.reranker import ConfigurableReranker

logger = logging.getLogger(__name__)


class KnowledgeService:
    """
    Core orchestrator for knowledge ingestion, chunking, hybrid vector indexing,
    reranked retrieval, and evaluation benchmarks.
    """

    def __init__(
        self,
        vector_store: BaseVectorStore | None = None,
        embedder: BaseEmbedder | None = None,
        reranker: BaseReranker | None = None,
        chunker: HeadingAwareChunker | None = None,
    ):
        self.chunker = chunker or HeadingAwareChunker()
        self.embedder = embedder or HybridEmbedder(
            dense_model_name=settings.EMBEDDING_MODEL,
            sparse_model_name=settings.SPARSE_EMBEDDING_MODEL,
            prefer_fastembed=settings.EMBEDDING_PROVIDER == "fastembed",
        )
        self.vector_store = vector_store or QdrantVectorStore(
            collection_name=settings.QDRANT_COLLECTION,
            dense_dim=self.embedder.dense_dimension,
            url=settings.QDRANT_URL,
            local_path=settings.QDRANT_LOCAL_PATH,
        )
        self.reranker = reranker or ConfigurableReranker(
            enabled=settings.RERANKER_ENABLED,
            model_name=settings.RERANKER_MODEL,
        )

    async def ingest_document(
        self, request: KnowledgeIngestRequest, db: AsyncSession
    ) -> SourceResponse:
        # Create Source record in PostgreSQL
        source_id = uuid.uuid4()
        source = Source(
            id=source_id,
            title=request.title,
            collection=request.collection,
            origin_url=request.origin_url,
            licence=request.licence,
            permission_notes=request.permission_notes,
            publication_date=request.publication_date,
            version=request.version,
            refresh_date=request.refresh_date,
            chunk_count=0,
        )
        db.add(source)
        await db.flush()

        # Chunk content
        chunks = self.chunker.chunk_markdown(
            content=request.content,
            source_id=str(source_id),
            title=request.title,
            collection=request.collection,
            licence=request.licence,
            publication_date=request.publication_date,
            tags=request.tags,
        )

        if chunks:
            # Batch embedding
            chunk_texts = [f"{c.title}\n{c.section_path}\n{c.text}" for c in chunks]
            dense_vecs, sparse_idxs, sparse_vals = await self.embedder.embed_documents(
                chunk_texts
            )

            for chunk, d_vec, s_idx, s_val in zip(
                chunks, dense_vecs, sparse_idxs, sparse_vals, strict=False
            ):
                chunk.dense_vector = d_vec
                chunk.sparse_indices = s_idx
                chunk.sparse_values = s_val

            # Index into Qdrant
            await self.vector_store.upsert_chunks(chunks)
            source.chunk_count = len(chunks)

        await db.commit()
        await db.refresh(source)
        return SourceResponse.model_validate(source)

    async def search(self, query: SearchQuery) -> SearchResponse:
        # Generate query dense and sparse embeddings
        dense_vec, s_idx, s_val = await self.embedder.embed_query(query.query)

        # Retrieve top candidates (fetch 2.5x limit to supply to reranker)
        candidate_limit = query.limit * 3 if query.use_reranker else query.limit
        candidates = await self.vector_store.search(
            dense_vector=dense_vec,
            sparse_indices=s_idx,
            sparse_values=s_val,
            limit=candidate_limit,
            filter=query.filter,
        )

        # Apply reranker if requested
        if query.use_reranker and candidates:
            final_results = await self.reranker.rerank(
                query=query.query,
                candidates=candidates,
                top_k=query.limit,
            )
        else:
            final_results = candidates[: query.limit]

        # Apply min_score threshold
        if query.min_score > 0.0:
            final_results = [r for r in final_results if r.score >= query.min_score]

        return SearchResponse(
            query=query.query,
            results=final_results,
            total=len(final_results),
            retrieval_mode=(
                "hybrid_rrf_reranked" if query.use_reranker else "hybrid_rrf"
            ),
        )

    async def list_sources(
        self, collection: str | None, db: AsyncSession
    ) -> list[SourceResponse]:
        stmt = select(Source)
        if collection:
            stmt = stmt.where(Source.collection == collection)
        stmt = stmt.order_by(Source.ingested_at.desc())
        res = await db.execute(stmt)
        sources = res.scalars().all()
        return [SourceResponse.model_validate(s) for s in sources]

    async def get_source(
        self, source_id: uuid.UUID, db: AsyncSession
    ) -> SourceResponse | None:
        stmt = select(Source).where(Source.id == source_id)
        res = await db.execute(stmt)
        source = res.scalar_one_or_none()
        return SourceResponse.model_validate(source) if source else None

    async def seed_default_documents(self, db: AsyncSession) -> int:
        """Seed 20–30 permitted documents across 5 collections."""
        from pathlib import Path

        seed_dir = Path(__file__).resolve().parents[3] / "data" / "seed_knowledge"

        if not seed_dir.exists():
            logger.warning("Seed directory not found at %s", seed_dir)
            return 0

        seeded_count = 0
        for collection_dir in os.listdir(seed_dir):
            coll_path = seed_dir / collection_dir
            if not coll_path.is_dir():
                continue

            for fname in os.listdir(coll_path):
                if not fname.endswith(".md"):
                    continue
                file_path = coll_path / fname
                with open(file_path, encoding="utf-8") as f:
                    content = f.read()

                # Parse frontmatter / header metadata
                title = fname.replace(".md", "").replace("_", " ").title()
                licence = "CC-BY-4.0"
                pub_date = "2024-01-01"
                tags = [str(collection_dir), fname.replace(".md", "")]

                # Check if already seeded by title
                stmt = select(Source).where(Source.title == title)
                existing = (await db.execute(stmt)).scalar_one_or_none()
                if existing:
                    continue

                req = KnowledgeIngestRequest(
                    title=title,
                    collection=collection_dir,  # type: ignore[arg-type]
                    content=content,
                    licence=licence,
                    publication_date=pub_date,
                    tags=tags,
                )
                await self.ingest_document(req, db)
                seeded_count += 1

        logger.info("Successfully seeded %d knowledge documents.", seeded_count)
        return seeded_count

    async def run_evaluation(self, db: AsyncSession) -> EvalRunResult:
        """
        Runs evaluation on 10 hand-written benchmark questions.
        Calculates MRR, Recall@3, and Recall@5.
        """
        from pathlib import Path

        eval_path = Path(__file__).resolve().parents[3] / "data" / "eval_questions.json"

        if not eval_path.exists():
            raise FileNotFoundError(f"Evaluation benchmark file missing at {eval_path}")

        with open(eval_path, encoding="utf-8") as f:
            eval_data = json.load(f)

        total = len(eval_data)
        reciprocal_ranks: list[float] = []
        hits_at_3 = 0
        hits_at_5 = 0
        details: list[dict] = []

        for item in eval_data:
            q_text = item["question"]
            gold_topics = [t.lower() for t in item.get("gold_topics", [])]

            search_res = await self.search(
                SearchQuery(query=q_text, limit=5, use_reranker=True)
            )

            # Check top 5 for gold topic matches
            hit_rank: int | None = None
            for idx, r in enumerate(search_res.results, start=1):
                haystack = f"{r.title} {r.section_path} {r.text}".lower()
                if any(topic in haystack for topic in gold_topics):
                    if hit_rank is None:
                        hit_rank = idx
                    break

            if hit_rank is not None:
                reciprocal_ranks.append(1.0 / hit_rank)
                if hit_rank <= 3:
                    hits_at_3 += 1
                if hit_rank <= 5:
                    hits_at_5 += 1
            else:
                reciprocal_ranks.append(0.0)

            details.append(
                {
                    "id": item["id"],
                    "question": q_text,
                    "hit_rank": hit_rank,
                    "top_chunk_title": (
                        search_res.results[0].title if search_res.results else None
                    ),
                    "top_chunk_section": (
                        search_res.results[0].section_path
                        if search_res.results
                        else None
                    ),
                }
            )

        mrr = round(sum(reciprocal_ranks) / max(1, total), 4)
        recall_at_3 = round(hits_at_3 / max(1, total), 4)
        recall_at_5 = round(hits_at_5 / max(1, total), 4)
        passed = recall_at_5 >= 0.8  # 80%+ recall definition of done

        # Record in eval_runs table
        eval_run = EvalRun(
            config={
                "embedding_model": settings.EMBEDDING_MODEL,
                "sparse_model": settings.SPARSE_EMBEDDING_MODEL,
                "reranker": settings.RERANKER_MODEL,
            },
            metrics={
                "total_questions": total,
                "mrr": mrr,
                "recall_at_3": recall_at_3,
                "recall_at_5": recall_at_5,
                "passed": passed,
            },
        )
        db.add(eval_run)
        await db.commit()

        return EvalRunResult(
            total_questions=total,
            mrr=mrr,
            recall_at_3=recall_at_3,
            recall_at_5=recall_at_5,
            passed=passed,
            details=details,
        )


# Singleton factory
_knowledge_service: KnowledgeService | None = None


def get_knowledge_service() -> KnowledgeService:
    global _knowledge_service
    if _knowledge_service is None:
        _knowledge_service = KnowledgeService()
    return _knowledge_service
