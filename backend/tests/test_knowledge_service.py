import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.knowledge import KnowledgeIngestRequest, SearchQuery
from app.services.knowledge.service import KnowledgeService


@pytest.mark.asyncio
async def test_knowledge_service_ingest_and_search(
    test_db: AsyncSession, test_knowledge_service: KnowledgeService
):
    req = KnowledgeIngestRequest(
        title="Cache-Aside Pattern Guide",
        collection="patterns",
        content="""# Cache-Aside Pattern
## Mechanism
Application queries Redis first. On cache miss, it queries PostgreSQL.

## Invalidation
On write, application deletes the cache key to avoid race conditions.
""",
        licence="CC-BY-4.0",
        tags=["cache", "redis", "postgres"],
    )

    source = await test_knowledge_service.ingest_document(req, test_db)
    assert source.title == "Cache-Aside Pattern Guide"
    assert source.chunk_count > 0

    # Search for cache invalidation
    search_res = await test_knowledge_service.search(
        SearchQuery(query="how to invalidate cache key on write", limit=5)
    )
    assert search_res.total > 0
    top_result = search_res.results[0]
    assert "Cache-Aside" in top_result.title
    assert "Invalidation" in top_result.section_path


@pytest.mark.asyncio
async def test_seed_and_evaluation_benchmark(
    test_db: AsyncSession, test_knowledge_service: KnowledgeService
):
    # Seed all 25 default documents across 5 collections
    seeded = await test_knowledge_service.seed_default_documents(test_db)
    assert seeded == 25

    # Run evaluation across 10 hand-written benchmark questions
    eval_result = await test_knowledge_service.run_evaluation(test_db)

    assert eval_result.total_questions == 10
    assert eval_result.mrr > 0.5
    assert eval_result.recall_at_5 >= 0.8  # Definition of done: >= 80% recall
    assert eval_result.passed is True
