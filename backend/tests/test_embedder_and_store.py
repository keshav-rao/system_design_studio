import pytest

from app.schemas.knowledge import KnowledgeChunk, KnowledgeFilter
from app.services.knowledge.providers.hybrid_embedder import HybridEmbedder
from app.services.knowledge.providers.qdrant_store import QdrantVectorStore
from app.services.knowledge.providers.reranker import ConfigurableReranker


@pytest.mark.asyncio
async def test_hybrid_embedder_dense_and_sparse():
    embedder = HybridEmbedder(prefer_fastembed=False)
    dense, s_idx, s_val = await embedder.embed_query("consistent hashing virtual nodes")

    assert len(dense) == embedder.dense_dimension
    assert len(s_idx) > 0
    assert len(s_idx) == len(s_val)

    # Test batch document embedding
    doc_dense, doc_s_idx, doc_s_val = await embedder.embed_documents(
        ["Document one about sharding", "Document two about redis cache"]
    )
    assert len(doc_dense) == 2
    assert len(doc_s_idx) == 2
    assert len(doc_s_val) == 2


@pytest.mark.asyncio
async def test_qdrant_hybrid_store_operations():
    store = QdrantVectorStore(collection_name="test_hybrid_ops", force_memory=True)
    embedder = HybridEmbedder(prefer_fastembed=False)

    # Create test chunks
    c1 = KnowledgeChunk(
        id="c1",
        source_id="src-1",
        collection="foundations",
        title="Consistent Hashing",
        section_path="Foundations > Hashing",
        licence="CC-BY-4.0",
        publication_date="2024-01-01",
        tags=["distributed", "hashing"],
        text="Consistent hashing ring distributes partition tokens evenly.",
    )
    c2 = KnowledgeChunk(
        id="c2",
        source_id="src-2",
        collection="patterns",
        title="Cache-Aside Pattern",
        section_path="Patterns > Caching",
        licence="MIT",
        publication_date="2024-01-01",
        tags=["caching", "performance"],
        text="Application invalidates redis key directly after write commit.",
    )

    # Embed chunks
    d_vecs, s_idxs, s_vals = await embedder.embed_documents([c1.text, c2.text])
    c1.dense_vector, c1.sparse_indices, c1.sparse_values = (
        d_vecs[0],
        s_idxs[0],
        s_vals[0],
    )
    c2.dense_vector, c2.sparse_indices, c2.sparse_values = (
        d_vecs[1],
        s_idxs[1],
        s_vals[1],
    )

    # Upsert
    inserted = await store.upsert_chunks([c1, c2])
    assert inserted == 2
    count = await store.count()
    assert count == 2

    # Query matching c1
    q_dense, q_s_idx, q_s_val = await embedder.embed_query("consistent hashing tokens")
    results = await store.search(
        dense_vector=q_dense,
        sparse_indices=q_s_idx,
        sparse_values=q_s_val,
        limit=5,
    )
    assert len(results) > 0
    assert results[0].title == "Consistent Hashing"

    # Query with collection filter
    filtered_results = await store.search(
        dense_vector=q_dense,
        sparse_indices=q_s_idx,
        sparse_values=q_s_val,
        limit=5,
        filter=KnowledgeFilter(collections=["patterns"]),
    )
    assert len(filtered_results) == 1
    assert filtered_results[0].collection == "patterns"

    # Delete by source
    await store.delete_by_source("src-1")
    count_after = await store.count()
    assert count_after == 1


@pytest.mark.asyncio
async def test_configurable_reranker():
    reranker = ConfigurableReranker(enabled=True)
    from app.schemas.knowledge import SearchResult

    candidates = [
        SearchResult(
            chunk_id="c1",
            source_id="s1",
            title="General Database Overview",
            collection="foundations",
            section_path="Overview",
            text="Relational databases use tables.",
            score=0.4,
            licence="CC-BY-4.0",
        ),
        SearchResult(
            chunk_id="c2",
            source_id="s2",
            title="Consistent Hashing Ring",
            collection="foundations",
            section_path="Foundations > Hashing > Virtual Nodes",
            text="Consistent hashing prevents cache stampedes when adding nodes.",
            score=0.42,
            licence="CC-BY-4.0",
        ),
    ]

    reranked = await reranker.rerank(
        query="consistent hashing virtual nodes",
        candidates=candidates,
        top_k=2,
    )

    assert len(reranked) == 2
    # The consistent hashing chunk should receive a higher score boost
    # and be ranked first
    assert reranked[0].chunk_id == "c2"
    assert reranked[0].score > reranked[1].score
