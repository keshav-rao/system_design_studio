import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_knowledge_api_flow(async_client: AsyncClient):
    # 1. Ingest via API
    ingest_payload = {
        "title": "Circuit Breaker Pattern",
        "collection": "patterns",
        "content": """# Circuit Breaker
## States
Closed, Open, and Half-Open.
When error threshold exceeds 50%, circuit trips open to prevent cascading failures.
""",
        "licence": "CC-BY-4.0",
        "tags": ["resilience", "microservices"],
    }
    resp = await async_client.post("/api/v1/knowledge/ingest", json=ingest_payload)
    assert resp.status_code == 201
    source_data = resp.json()
    assert source_data["title"] == "Circuit Breaker Pattern"
    assert source_data["chunk_count"] > 0
    source_id = source_data["id"]

    # 2. Get source by ID
    resp_get = await async_client.get(f"/api/v1/knowledge/sources/{source_id}")
    assert resp_get.status_code == 200
    assert resp_get.json()["id"] == source_id

    # 3. List sources
    resp_list = await async_client.get("/api/v1/knowledge/sources")
    assert resp_list.status_code == 200
    assert len(resp_list.json()) >= 1

    # 4. Search via API
    search_payload = {
        "query": "what states does circuit breaker have",
        "limit": 3,
        "use_reranker": True,
    }
    resp_search = await async_client.post(
        "/api/v1/knowledge/search", json=search_payload
    )
    assert resp_search.status_code == 200
    search_data = resp_search.json()
    assert search_data["total"] >= 1
    assert "Circuit Breaker" in search_data["results"][0]["title"]


@pytest.mark.asyncio
async def test_knowledge_seed_and_eval_endpoints(async_client: AsyncClient):
    # Seed endpoint
    resp_seed = await async_client.post("/api/v1/knowledge/seed")
    assert resp_seed.status_code == 200
    assert resp_seed.json()["seeded_sources"] == 25

    # Eval endpoint
    resp_eval = await async_client.post("/api/v1/knowledge/eval")
    assert resp_eval.status_code == 200
    eval_data = resp_eval.json()
    assert eval_data["total_questions"] == 10
    assert eval_data["recall_at_5"] >= 0.8
    assert eval_data["passed"] is True
