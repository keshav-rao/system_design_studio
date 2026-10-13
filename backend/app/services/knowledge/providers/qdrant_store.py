import logging
import uuid
from typing import Any

from qdrant_client import QdrantClient, models

from app.core.config import settings
from app.schemas.knowledge import KnowledgeChunk, KnowledgeFilter, SearchResult
from app.services.knowledge.interfaces.vector_store import BaseVectorStore

logger = logging.getLogger(__name__)


class QdrantVectorStore(BaseVectorStore):
    """
    Qdrant hybrid vector store supporting dense vectors, sparse BM25 vectors,
    payload filtering, and Reciprocal Rank Fusion (RRF).
    Supports remote Qdrant and falls back to local embedded/in-memory mode.
    """

    def __init__(
        self,
        collection_name: str = settings.QDRANT_COLLECTION,
        dense_dim: int = 384,
        url: str | None = settings.QDRANT_URL,
        local_path: str | None = settings.QDRANT_LOCAL_PATH,
        force_memory: bool = False,
    ):
        self.collection_name = collection_name
        self.dense_dim = dense_dim
        self.url = url
        self.local_path = local_path
        self.force_memory = force_memory
        self.client: QdrantClient = self._connect()

    def _connect(self) -> QdrantClient:
        if self.force_memory:
            logger.info("Initializing in-memory Qdrant client")
            return QdrantClient(":memory:")

        # Try connecting to configured URL
        if self.url and not self.url.startswith("file"):
            try:
                client = QdrantClient(url=self.url, timeout=2)
                # Quick probe to see if remote server is alive
                client.get_collections()
                logger.info("Connected to remote Qdrant server at %s", self.url)
                return client
            except Exception as e:
                logger.info(
                    "Remote Qdrant unavailable (%s), "
                    "falling back to local persistent store at %s",
                    e,
                    self.local_path,
                )

        try:
            return QdrantClient(path=self.local_path)
        except Exception as e:
            logger.warning("Local Qdrant storage failed (%s), using in-memory mode", e)
            return QdrantClient(":memory:")

    async def initialize(self) -> None:
        """Create collection with dense and sparse vector configurations."""
        try:
            exists = self.client.collection_exists(self.collection_name)
        except Exception:
            exists = False

        if not exists:
            logger.info("Creating Qdrant collection: %s", self.collection_name)
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config={
                    "dense": models.VectorParams(
                        size=self.dense_dim,
                        distance=models.Distance.COSINE,
                    )
                },
                sparse_vectors_config={"sparse": models.SparseVectorParams()},
            )

            # Create payload indexes for fast filtering
            for field in ["collection", "licence", "source_id", "tags"]:
                try:
                    self.client.create_payload_index(
                        collection_name=self.collection_name,
                        field_name=field,
                        field_schema=models.PayloadSchemaType.KEYWORD,
                    )
                except Exception as e:
                    logger.debug("Payload index creation note: %s", e)

    async def upsert_chunks(self, chunks: list[KnowledgeChunk]) -> int:
        if not chunks:
            return 0

        await self.initialize()
        points: list[models.PointStruct] = []

        for chunk in chunks:
            point_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, chunk.id))
            dense_vec = chunk.dense_vector or [0.0] * self.dense_dim
            sparse_indices = chunk.sparse_indices or []
            sparse_values = chunk.sparse_values or []

            vector_dict: Any = {
                "dense": dense_vec,
                "sparse": models.SparseVector(
                    indices=sparse_indices,
                    values=sparse_values,
                ),
            }

            payload = {
                "chunk_id": chunk.id,
                "source_id": chunk.source_id,
                "collection": chunk.collection,
                "title": chunk.title,
                "section_path": chunk.section_path,
                "page": chunk.page,
                "licence": chunk.licence,
                "publication_date": chunk.publication_date,
                "tags": chunk.tags,
                "text": chunk.text,
                "token_count": chunk.token_count,
            }

            points.append(
                models.PointStruct(
                    id=point_id,
                    vector=vector_dict,
                    payload=payload,
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )
        return len(points)

    def _build_filter(
        self, filter_spec: KnowledgeFilter | None
    ) -> models.Filter | None:
        if not filter_spec:
            return None

        must_conditions: list[models.Condition] = []

        if filter_spec.collections:
            must_conditions.append(
                models.FieldCondition(
                    key="collection",
                    match=models.MatchAny(
                        any=[str(c) for c in filter_spec.collections]
                    ),
                )
            )

        if filter_spec.tags:
            must_conditions.append(
                models.FieldCondition(
                    key="tags",
                    match=models.MatchAny(any=filter_spec.tags),
                )
            )

        if filter_spec.licence:
            must_conditions.append(
                models.FieldCondition(
                    key="licence",
                    match=models.MatchValue(value=filter_spec.licence),
                )
            )

        if not must_conditions:
            return None

        return models.Filter(must=must_conditions)

    async def search(
        self,
        dense_vector: list[float] | None,
        sparse_indices: list[int] | None,
        sparse_values: list[float] | None,
        limit: int = 10,
        filter: KnowledgeFilter | None = None,
    ) -> list[SearchResult]:
        await self.initialize()
        q_filter = self._build_filter(filter)

        prefetch: list[models.Prefetch] = []

        if dense_vector:
            prefetch.append(
                models.Prefetch(
                    query=dense_vector,
                    using="dense",
                    limit=limit * 2,
                    filter=q_filter,
                )
            )

        if sparse_indices and sparse_values:
            prefetch.append(
                models.Prefetch(
                    query=models.SparseVector(
                        indices=sparse_indices,
                        values=sparse_values,
                    ),
                    using="sparse",
                    limit=limit * 2,
                    filter=q_filter,
                )
            )

        if not prefetch:
            return []

        if len(prefetch) > 1:
            query_res = self.client.query_points(
                collection_name=self.collection_name,
                prefetch=prefetch,
                query=models.FusionQuery(fusion=models.Fusion.RRF),
                limit=limit,
                with_payload=True,
            )
        else:
            # Single prefetch branch fallback
            p = prefetch[0]
            query_res = self.client.query_points(
                collection_name=self.collection_name,
                query=p.query,
                using=p.using,
                limit=limit,
                filter=q_filter,
                with_payload=True,
            )

        results: list[SearchResult] = []
        for point in query_res.points:
            payload = point.payload or {}
            results.append(
                SearchResult(
                    chunk_id=payload.get("chunk_id", str(point.id)),
                    source_id=payload.get("source_id", ""),
                    title=payload.get("title", ""),
                    collection=payload.get("collection", ""),
                    section_path=payload.get("section_path", ""),
                    text=payload.get("text", ""),
                    score=float(point.score or 0.0),
                    licence=payload.get("licence", "unknown"),
                    publication_date=payload.get("publication_date"),
                    tags=payload.get("tags", []),
                    page=payload.get("page"),
                )
            )

        return results

    async def delete_by_source(self, source_id: str) -> int:
        await self.initialize()
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=models.FilterSelector(
                filter=models.Filter(
                    must=[
                        models.FieldCondition(
                            key="source_id",
                            match=models.MatchValue(value=source_id),
                        )
                    ]
                )
            ),
        )
        return 1

    async def count(self) -> int:
        await self.initialize()
        try:
            info = self.client.get_collection(self.collection_name)
            return info.points_count or 0
        except Exception:
            return 0
