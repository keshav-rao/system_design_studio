import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_catalog_api_seed_and_query(async_client: AsyncClient) -> None:
    # 1. Seed catalog
    seed_res = await async_client.post("/api/v1/catalog/seed?force=true")
    assert seed_res.status_code == 200
    data = seed_res.json()
    assert data["components_total"] >= 35

    # 2. List components
    list_res = await async_client.get("/api/v1/catalog/components")
    assert list_res.status_code == 200
    list_data = list_res.json()
    assert list_data["total"] >= 35
    assert len(list_data["items"]) >= 35

    # 3. Filter by category
    filter_res = await async_client.get("/api/v1/catalog/components?category=database")
    assert filter_res.status_code == 200
    filter_data = filter_res.json()
    assert filter_data["total"] >= 5
    for item in filter_data["items"]:
        assert item["category"] == "database"

    # 4. Get specific component by slug
    comp_res = await async_client.get("/api/v1/catalog/components/postgresql")
    assert comp_res.status_code == 200
    comp_data = comp_res.json()
    assert comp_data["slug"] == "postgresql"
    assert "limits" in comp_data
    assert "failure_modes" in comp_data
    assert "cost_units" in comp_data

    # 404 for missing component
    missing_res = await async_client.get("/api/v1/catalog/components/not-existing-comp")
    assert missing_res.status_code == 404


@pytest.mark.asyncio
async def test_catalog_api_compatibility_checks(async_client: AsyncClient) -> None:
    # Seed
    await async_client.post("/api/v1/catalog/seed?force=true")

    # 1. Valid compatibility check
    compat_res = await async_client.get(
        "/api/v1/catalog/compatibility/check",
        params={"source": "fastapi-app-server", "target": "postgresql"},
    )
    assert compat_res.status_code == 200
    compat_data = compat_res.json()
    assert compat_data["compatible"] is True
    assert compat_data["protocol"] == "TCP/SQL"
    assert "effective_throughput_qps" in compat_data["limits"]

    # 2. Invalid compatibility check (Antipattern)
    antipattern_res = await async_client.get(
        "/api/v1/catalog/compatibility/check",
        params={"source": "cloudflare-cdn", "target": "postgresql"},
    )
    assert antipattern_res.status_code == 200
    antipattern_data = antipattern_res.json()
    assert antipattern_data["compatible"] is False
    assert "ANTIPATTERN" in antipattern_data["reason"]


@pytest.mark.asyncio
async def test_catalog_api_crud_flow(async_client: AsyncClient) -> None:
    # 1. Create component
    payload = {
        "slug": "custom-queue-broker",
        "name": "Custom Queue Broker",
        "category": "queue",
        "layer": "async",
        "description": "High-throughput custom queue",
        "protocols": ["TCP", "AMQP"],
        "limits": {"max_throughput_qps": 30000},
        "failure_modes": [],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/mo",
            "base_monthly_usd": 15.0,
        },
        "alternatives": ["rabbitmq"],
        "is_active": True,
    }
    create_res = await async_client.post("/api/v1/catalog/components", json=payload)
    assert create_res.status_code == 201
    created_data = create_res.json()
    comp_id = created_data["id"]

    # 2. Duplicate slug error (409 Conflict)
    dup_res = await async_client.post("/api/v1/catalog/components", json=payload)
    assert dup_res.status_code == 409

    # 3. Update component
    update_res = await async_client.put(
        f"/api/v1/catalog/components/{comp_id}",
        json={"name": "Updated Custom Queue Broker"},
    )
    assert update_res.status_code == 200
    assert update_res.json()["name"] == "Updated Custom Queue Broker"

    # 4. Add compatibility edge
    edge_payload = {
        "source_slug": "custom-queue-broker",
        "target_slug": "celery-worker",
        "is_compatible": True,
        "protocol": "AMQP",
        "recommended_pattern": "Worker Task Consumer",
        "constraints": {},
        "reason": "Celery consumes from custom queue broker",
    }
    edge_res = await async_client.post(
        "/api/v1/catalog/compatibility", json=edge_payload
    )
    assert edge_res.status_code == 201
    assert edge_res.json()["is_compatible"] is True

    # 5. Delete component
    del_res = await async_client.delete(f"/api/v1/catalog/components/{comp_id}")
    assert del_res.status_code == 204

    # Confirm deletion
    get_res = await async_client.get(f"/api/v1/catalog/components/{comp_id}")
    assert get_res.status_code == 404
