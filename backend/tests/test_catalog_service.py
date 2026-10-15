import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.catalog import (
    CompatibilityEdgeCreate,
    ComponentCreate,
    ComponentUpdate,
)
from app.services.catalog.catalog_service import catalog_service


@pytest.mark.asyncio
async def test_seed_and_get_components(test_db: AsyncSession) -> None:
    # 1. Seed catalog
    seed_stats = await catalog_service.seed_catalog(test_db, force=True)
    assert seed_stats["components_total"] >= 35
    assert seed_stats["components_inserted"] >= 35
    assert seed_stats["edges_total"] >= 15

    # 2. Get components list
    components, total = await catalog_service.get_components(test_db)
    assert total >= 35
    assert len(components) == total

    # 3. Filter by category
    db_components, db_total = await catalog_service.get_components(
        test_db, category="database"
    )
    assert db_total >= 5
    for c in db_components:
        assert c.category == "database"

    # 4. Filter by layer
    edge_components, edge_total = await catalog_service.get_components(
        test_db, layer="edge"
    )
    assert edge_total >= 2
    for c in edge_components:
        assert c.layer == "edge"

    # 5. Search keyword
    pg_results, pg_total = await catalog_service.get_components(
        test_db, search="postgres"
    )
    assert pg_total >= 1
    assert any("postgres" in c.slug.lower() for c in pg_results)


@pytest.mark.asyncio
async def test_component_crud_operations(test_db: AsyncSession) -> None:
    # Create
    comp_in = ComponentCreate(
        slug="test-rust-service",
        name="Rust High-Performance Service",
        category="compute",
        layer="application",
        description="Low latency microservice written in Actix Web / Axum",
        protocols=["HTTP", "gRPC"],
        limits={"max_throughput_qps": 80000, "latency_p99_ms": 2},
        failure_modes=[
            {
                "mode": "Compile time safe, runtime panic",
                "impact": "Worker crashes on unwrap",
                "mitigation": "Proper Result/Option error handling",
            }
        ],
        cost_units={
            "model": "provisioned",
            "unit": "$/month",
            "base_monthly_usd": 20.0,
        },
        alternatives=["go-microservice"],
        is_active=True,
    )
    comp = await catalog_service.create_component(test_db, comp_in)
    assert comp.id is not None
    assert comp.slug == "test-rust-service"

    # Read by slug and by id
    by_slug = await catalog_service.get_component_by_slug_or_id(
        test_db, "test-rust-service"
    )
    assert by_slug is not None
    assert by_slug.name == "Rust High-Performance Service"

    by_id = await catalog_service.get_component_by_slug_or_id(test_db, str(comp.id))
    assert by_id is not None
    assert by_id.slug == "test-rust-service"

    # Update
    updated = await catalog_service.update_component(
        test_db,
        comp.id,
        ComponentUpdate(name="Rust Axum Service", description="Updated description"),
    )
    assert updated is not None
    assert updated.name == "Rust Axum Service"
    assert updated.description == "Updated description"

    # Delete
    deleted = await catalog_service.delete_component(test_db, comp.id)
    assert deleted is True

    # Confirm non-existence
    assert (
        await catalog_service.get_component_by_slug_or_id(test_db, str(comp.id)) is None
    )


@pytest.mark.asyncio
async def test_compatibility_engine(test_db: AsyncSession) -> None:
    # Seed standard catalog
    await catalog_service.seed_catalog(test_db, force=True)

    # 1. Valid connection: FastAPI -> PostgreSQL
    res = await catalog_service.check_compatibility(
        test_db, "fastapi-app-server", "postgresql"
    )
    assert res.compatible is True
    assert res.protocol == "TCP/SQL"
    assert "PgBouncer" in str(res.recommended_pattern)
    assert res.limits["effective_throughput_qps"] is not None

    # 2. Invalid connection: Cloudflare CDN directly to PostgreSQL
    res_inval = await catalog_service.check_compatibility(
        test_db, "cloudflare-cdn", "postgresql"
    )
    assert res_inval.compatible is False
    assert "ANTIPATTERN" in res_inval.reason

    # 3. Invalid connection: Database directly to Kafka without CDC/Outbox
    res_db_kafka = await catalog_service.check_compatibility(
        test_db, "postgresql", "apache-kafka"
    )
    assert res_db_kafka.compatible is False
    assert "Outbox" in res_db_kafka.reason or "CDC" in res_db_kafka.reason

    # 4. Fallback rule: Edge directly to Database
    # Test with custom edge and db components without explicit edge
    custom_edge = await catalog_service.create_component(
        test_db,
        ComponentCreate(
            slug="fastly-edge",
            name="Fastly VCL CDN",
            category="cdn",
            layer="edge",
            description="Edge CDN",
            protocols=["HTTPS"],
        ),
    )
    res_edge_db = await catalog_service.check_compatibility(
        test_db, custom_edge.slug, "mysql"
    )
    assert res_edge_db.compatible is False
    assert "ANTIPATTERN" in res_edge_db.reason

    # 5. Non-existent components
    res_missing = await catalog_service.check_compatibility(
        test_db, "non-existent-comp", "postgresql"
    )
    assert res_missing.compatible is False
    assert "not found" in res_missing.reason

    # 6. Dynamic edge addition
    custom_edge_def = await catalog_service.add_compatibility_edge(
        test_db,
        CompatibilityEdgeCreate(
            source_slug="fastly-edge",
            target_slug="nginx-reverse-proxy",
            is_compatible=True,
            protocol="HTTPS",
            recommended_pattern="Strict TLS Origin",
            reason="Fastly forwards misses to NGINX",
        ),
    )
    assert custom_edge_def.is_compatible is True

    res_custom = await catalog_service.check_compatibility(
        test_db, "fastly-edge", "nginx-reverse-proxy"
    )
    assert res_custom.compatible is True
    assert res_custom.protocol == "HTTPS"
