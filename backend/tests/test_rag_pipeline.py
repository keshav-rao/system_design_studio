"""LlamaIndex RAG pipeline: corpus loading, chunking, bge-m3 embedder, reranking."""

import json
from pathlib import Path

import numpy as np
import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.models.source import Source
from app.schemas.knowledge import KnowledgeIngestRequest, SearchQuery, SearchResult
from app.services.knowledge.ingestion.corpus_loader import (
    ROOT_COLLECTION,
    iter_corpus_documents,
)
from app.services.knowledge.ingestion.llama_chunker import LlamaIndexChunker
from app.services.knowledge.providers.bge_m3_embedder import BGEM3Embedder
from app.services.knowledge.providers.factory import build_embedder
from app.services.knowledge.providers.hybrid_embedder import HybridEmbedder
from app.services.knowledge.providers.qdrant_store import QdrantVectorStore
from app.services.knowledge.providers.reranker import ConfigurableReranker
from app.services.knowledge.service import KnowledgeService


@pytest.fixture
def corpus(tmp_path: Path) -> Path:
    (tmp_path / "01_fundamentals").mkdir()
    (tmp_path / "01_fundamentals" / "cap.md").write_text(
        "# CAP Theorem\n## Partitions\nDuring a network partition choose C or A.\n"
    )
    (tmp_path / "redis-docs" / "develop").mkdir(parents=True)
    (tmp_path / "redis-docs" / "develop" / "streams.md").write_text(
        "# Redis Streams\nConsumer groups let workers share a stream.\n"
    )
    (tmp_path / "redis-docs" / "develop" / "MANIFEST.json").write_text(
        json.dumps({"docset": "develop", "title": "Develop"})
    )
    (tmp_path / "book.md").write_text("Designing data-intensive applications.\n")
    (tmp_path / "image.png").write_bytes(b"\x89PNG")
    (tmp_path / "corpus_manifest.json").write_text(
        json.dumps(
            {
                "documents": [
                    {
                        "path": "01_fundamentals/cap.md",
                        "licence": "CC-BY-4.0",
                        "source_url": "https://en.wikipedia.org/wiki/CAP_theorem",
                        "topic": "distributed_systems_theory",
                    }
                ]
            }
        )
    )
    return tmp_path


def test_corpus_loader_reads_every_folder_and_manifest(corpus: Path) -> None:
    docs = {d.rel_path: d for d in iter_corpus_documents(corpus)}

    assert set(docs) == {
        "01_fundamentals/cap.md",
        "redis-docs/develop/streams.md",
        "redis-docs/develop/MANIFEST.json",
        "book.md",
        "corpus_manifest.json",
    }
    cap = docs["01_fundamentals/cap.md"]
    assert cap.title == "CAP Theorem"
    assert cap.collection == "01_fundamentals"
    assert cap.licence == "CC-BY-4.0"
    assert cap.origin_url == "https://en.wikipedia.org/wiki/CAP_theorem"
    assert "distributed_systems_theory" in cap.tags
    assert docs["redis-docs/develop/streams.md"].tags == ["redis-docs", "develop"]
    assert docs["book.md"].collection == ROOT_COLLECTION
    assert docs["book.md"].licence == "unspecified"

    only = list(iter_corpus_documents(corpus, collections=["redis-docs"]))
    assert {d.collection for d in only} == {"redis-docs"}


def test_llamaindex_chunker_keeps_heading_path_and_bounds_size() -> None:
    chunker = LlamaIndexChunker(chunk_size=64, chunk_overlap=8)
    body = "Replicas copy the leader log. " * 40
    chunks = chunker.chunk_markdown(
        f"# Databases\nIntro.\n## Replication\n{body}",
        source_id="s1",
        title="DB Guide",
        collection="01_fundamentals",
    )

    replication = [c for c in chunks if c.section_path == "Databases > Replication"]
    assert len(replication) > 1
    assert all(len(c.text.split()) < 80 for c in replication)
    assert chunks[0].section_path == "Databases"
    assert len({c.id for c in chunks}) == len(chunks)


class _FakeM3:
    def __init__(self) -> None:
        self.calls: list[dict] = []

    def encode(self, texts: list[str], **kwargs: object) -> dict:
        self.calls.append(kwargs)
        return {
            "dense_vecs": np.ones((len(texts), 1024), dtype=np.float32),
            "lexical_weights": [{"42": 0.5, "7": 0.25} for _ in texts],
        }


@pytest.mark.asyncio
async def test_bge_m3_embedder_returns_dense_and_sorted_sparse() -> None:
    fake = _FakeM3()
    embedder = BGEM3Embedder(model=fake, batch_size=4, max_length=256)

    dense, idx, val = await embedder.embed_query("kafka vs rabbitmq")
    docs_dense, docs_idx, _ = await embedder.embed_documents(["a", "b"])

    assert embedder.dense_dimension == len(dense) == 1024
    assert idx == [7, 42] and val == [0.25, 0.5]
    assert len(docs_dense) == len(docs_idx) == 2
    assert fake.calls[0]["return_sparse"] is True
    assert fake.calls[0]["max_length"] == 256


def test_embedder_factory_and_strict_fastembed() -> None:
    assert isinstance(build_embedder("bge-m3"), BGEM3Embedder)
    assert isinstance(build_embedder("hash"), HybridEmbedder)
    with pytest.raises(ValueError):
        build_embedder("nope")

    strict = HybridEmbedder(dense_model_name="not/a-model", strict=True)
    with pytest.raises(RuntimeError):
        strict._init_models()


@pytest.mark.asyncio
async def test_cross_encoder_reranker_uses_llamaindex_postprocessor() -> None:
    class FakeRerank:
        top_n = 0

        def postprocess_nodes(self, nodes, query_bundle):  # noqa: ANN001
            assert query_bundle.query_str == "q"
            ranked = sorted(nodes, key=lambda n: "redis" in n.node.text, reverse=True)
            for i, n in enumerate(ranked):
                n.score = 1.0 - i * 0.1
            return ranked[: self.top_n]

    def result(cid: str, title: str) -> SearchResult:
        return SearchResult(
            chunk_id=cid,
            source_id="s",
            title=title,
            collection="c",
            section_path="",
            text="",
            score=0.1,
            licence="x",
        )

    reranker = ConfigurableReranker(
        provider="cross-encoder", postprocessor=FakeRerank()
    )
    out = await reranker.rerank(
        "q", [result("a", "postgres"), result("b", "redis")], top_k=1
    )

    assert [r.chunk_id for r in out] == ["b"]
    assert out[0].score == 1.0


@pytest.mark.asyncio
async def test_qdrant_rejects_dimension_mismatch() -> None:
    small = QdrantVectorStore(collection_name="dims", dense_dim=8, force_memory=True)
    await small.initialize()
    big = QdrantVectorStore(collection_name="dims", dense_dim=16, force_memory=True)
    big.client = small.client

    with pytest.raises(RuntimeError, match="--recreate"):
        await big.initialize()
    await big.recreate()
    assert await big.count() == 0


@pytest.mark.asyncio
async def test_ingest_corpus_is_idempotent_and_searchable(
    test_db: AsyncSession, test_knowledge_service: KnowledgeService, corpus: Path
) -> None:
    first = await test_knowledge_service.ingest_corpus(test_db, corpus)
    assert first["ingested"] == 5 and first["chunks"] > 0

    second = await test_knowledge_service.ingest_corpus(test_db, corpus)
    assert second == {
        "ingested": 0,
        "updated": 0,
        "skipped": 5,
        "deleted": 0,
        "chunks": 0,
    }

    (corpus / "01_fundamentals" / "cap.md").write_text(
        "# CAP Theorem\nPACELC extends CAP with latency.\n"
    )
    third = await test_knowledge_service.ingest_corpus(test_db, corpus)
    assert third["updated"] == 1 and third["skipped"] == 4

    sources = (await test_db.execute(select(Source))).scalars().all()
    assert len(sources) == 5
    res = await test_knowledge_service.search(
        SearchQuery(query="redis streams consumer groups", limit=3)
    )
    assert res.results[0].collection == "redis-docs"


@pytest.mark.asyncio
async def test_ingest_corpus_reindexes_on_manifest_change_and_drops_deleted_files(
    test_db: AsyncSession,
    test_knowledge_service: KnowledgeService,
    corpus: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(settings, "RAG_CORPUS_PATH", str(corpus))
    await test_knowledge_service.ingest_corpus(test_db, corpus)

    manifest = json.loads((corpus / "corpus_manifest.json").read_text())
    manifest["documents"][0]["licence"] = "restricted"
    (corpus / "corpus_manifest.json").write_text(json.dumps(manifest))
    (corpus / "redis-docs" / "develop" / "streams.md").unlink()

    stats = await test_knowledge_service.ingest_corpus(test_db, corpus)

    assert stats["deleted"] == 1
    assert stats["updated"] == 2  # cap.md (licence) + corpus_manifest.json itself
    sources = {s.title: s for s in (await test_db.execute(select(Source))).scalars()}
    assert "Redis Streams" not in sources
    assert sources["CAP Theorem"].licence == "restricted"
    res = await test_knowledge_service.search(
        SearchQuery(query="redis streams consumer groups", limit=10)
    )
    assert all(r.title != "Redis Streams" for r in res.results)


@pytest.mark.asyncio
async def test_partial_scan_never_deletes_unvisited_sources(
    test_db: AsyncSession, test_knowledge_service: KnowledgeService, corpus: Path
) -> None:
    await test_knowledge_service.ingest_corpus(test_db, corpus)
    (corpus / "redis-docs" / "develop" / "streams.md").unlink()

    stats = await test_knowledge_service.ingest_corpus(
        test_db, corpus, collections=["01_fundamentals"]
    )

    assert stats["deleted"] == 0
    titles = {s.title for s in (await test_db.execute(select(Source))).scalars()}
    assert "Redis Streams" in titles


@pytest.mark.asyncio
async def test_failed_update_keeps_previous_vectors(
    test_db: AsyncSession, test_knowledge_service: KnowledgeService, corpus: Path
) -> None:
    await test_knowledge_service.ingest_corpus(test_db, corpus)
    before = await test_knowledge_service.vector_store.count()
    (corpus / "01_fundamentals" / "cap.md").write_text("# CAP Theorem\nChanged.\n")

    async def boom(texts: list[str]) -> None:
        raise RuntimeError("embedding model unavailable")

    test_knowledge_service.embedder.embed_documents = boom  # type: ignore[method-assign]
    with pytest.raises(RuntimeError):
        await test_knowledge_service.ingest_corpus(test_db, corpus)

    assert await test_knowledge_service.vector_store.count() == before
    res = await test_knowledge_service.search(
        SearchQuery(query="network partition choose", limit=5)
    )
    assert any("partition" in r.text.lower() for r in res.results)


@pytest.mark.asyncio
async def test_failure_in_later_batch_rolls_back_partial_replacement(
    test_db: AsyncSession,
    test_knowledge_service: KnowledgeService,
    corpus: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    await test_knowledge_service.ingest_corpus(test_db, corpus)
    before = await test_knowledge_service.vector_store.count()
    (corpus / "01_fundamentals" / "cap.md").write_text(
        "# CAP Theorem\n## Part one\nFirst replacement.\n"
        "## Part two\nSecond replacement.\n"
    )
    monkeypatch.setattr(settings, "EMBEDDING_BATCH_SIZE", 1)
    real_embed = test_knowledge_service.embedder.embed_documents
    calls = 0

    async def fail_second(texts: list[str]):  # type: ignore[no-untyped-def]
        nonlocal calls
        calls += 1
        if calls == 2:
            raise RuntimeError("embedding model unavailable")
        return await real_embed(texts)

    test_knowledge_service.embedder.embed_documents = fail_second  # type: ignore[method-assign]
    with pytest.raises(RuntimeError):
        await test_knowledge_service.ingest_corpus(test_db, corpus)

    assert calls == 2
    assert await test_knowledge_service.vector_store.count() == before
    res = await test_knowledge_service.search(
        SearchQuery(query="first replacement", limit=10)
    )
    assert all("replacement" not in r.text.lower() for r in res.results)


@pytest.mark.asyncio
async def test_pruning_skips_alternate_roots_and_uploaded_documents(
    test_db: AsyncSession,
    test_knowledge_service: KnowledgeService,
    corpus: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(settings, "RAG_CORPUS_PATH", str(corpus))
    await test_knowledge_service.ingest_corpus(test_db)
    await test_knowledge_service.ingest_document(
        KnowledgeIngestRequest(
            title="Uploaded runbook",
            collection="uploads",
            content="# Runbook\nRestart the worker pool.",
            permission_notes="rag_knowledge_base/uploads/runbook.md",
        ),
        test_db,
    )
    other = tmp_path / "other_corpus" / "notes"
    other.mkdir(parents=True)
    (other / "extra.md").write_text("# Extra\nSomething else.\n")

    alt = await test_knowledge_service.ingest_corpus(test_db, other.parent)
    full = await test_knowledge_service.ingest_corpus(test_db)

    assert alt["deleted"] == 0
    assert full["deleted"] == 1  # only the alternate-root file is pruned
    titles = {s.title for s in (await test_db.execute(select(Source))).scalars()}
    assert {"Redis Streams", "Uploaded runbook"} <= titles


def test_cli_rejects_partial_recreate() -> None:
    import subprocess
    import sys

    proc = subprocess.run(
        [sys.executable, "-m", "app.cli.ingest_corpus", "--recreate", "--limit", "1"],
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 2
    assert "--recreate rebuilds the whole index" in proc.stderr
