"""Tests for the validator service and all individual rules.

Each rule has at least one passing test (no issues) and one failing test
(issues detected). The full validator service is also tested for
aggregation and timing.
"""

from typing import Any

import pytest

from app.schemas.validator import (
    DesignDocument,
    DesignEdge,
    DesignNode,
    DesignRequirements,
    Severity,
)
from app.services.validator.rules import (
    async_processing,
    cache_before_db,
    data_store_required,
    gateway_required,
    multi_region,
    no_dangling_nodes,
    no_duplicate_edges,
    no_edge_to_db,
    no_self_loops,
    no_spof,
    throughput_bottleneck,
    valid_edge_refs,
)
from app.services.validator.validator_service import ValidatorService

# ---------------------------------------------------------------------------
# Helper factory
# ---------------------------------------------------------------------------

def _node(
    id: str,
    slug: str,
    category: str,
    layer: str,
    replicas: int = 1,
    limits: dict | None = None,
) -> DesignNode:
    return DesignNode(
        id=id,
        slug=slug,
        category=category,
        layer=layer,
        replicas=replicas,
        limits=limits or {},
    )


def _edge(src: str, tgt: str, protocol: str | None = None) -> DesignEdge:
    return DesignEdge(source_id=src, target_id=tgt, protocol=protocol)


# =========================================================================
# Rule: valid-edge-refs
# =========================================================================


class TestValidEdgeRefs:
    def test_pass_all_refs_valid(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("a", "nginx", "gateway", "edge"),
                _node("b", "fastapi", "compute", "application"),
            ],
            edges=[_edge("a", "b")],
        )
        issues = valid_edge_refs.validate(design)
        assert issues == []

    def test_fail_missing_target(self) -> None:
        design = DesignDocument(
            nodes=[_node("a", "nginx", "gateway", "edge")],
            edges=[_edge("a", "nonexistent")],
        )
        issues = valid_edge_refs.validate(design)
        assert len(issues) == 1
        assert issues[0].rule_id == "valid-edge-refs"
        assert issues[0].severity == Severity.ERROR
        assert "nonexistent" in issues[0].message

    def test_fail_missing_source(self) -> None:
        design = DesignDocument(
            nodes=[_node("b", "fastapi", "compute", "application")],
            edges=[_edge("ghost", "b")],
        )
        issues = valid_edge_refs.validate(design)
        assert len(issues) == 1
        assert issues[0].severity == Severity.ERROR


# =========================================================================
# Rule: no-self-loops
# =========================================================================


class TestNoSelfLoops:
    def test_pass_no_loops(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("a", "nginx", "gateway", "edge"),
                _node("b", "fastapi", "compute", "application"),
            ],
            edges=[_edge("a", "b")],
        )
        issues = no_self_loops.validate(design)
        assert issues == []

    def test_fail_self_loop(self) -> None:
        design = DesignDocument(
            nodes=[_node("a", "nginx", "gateway", "edge")],
            edges=[_edge("a", "a")],
        )
        issues = no_self_loops.validate(design)
        assert len(issues) == 1
        assert issues[0].rule_id == "no-self-loops"
        assert issues[0].severity == Severity.ERROR


# =========================================================================
# Rule: no-duplicate-edges
# =========================================================================


class TestNoDuplicateEdges:
    def test_pass_no_duplicates(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("a", "nginx", "gateway", "edge"),
                _node("b", "fastapi", "compute", "application"),
            ],
            edges=[_edge("a", "b")],
        )
        issues = no_duplicate_edges.validate(design)
        assert issues == []

    def test_fail_duplicate_edge(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("a", "nginx", "gateway", "edge"),
                _node("b", "fastapi", "compute", "application"),
            ],
            edges=[_edge("a", "b"), _edge("a", "b")],
        )
        issues = no_duplicate_edges.validate(design)
        assert len(issues) == 1
        assert issues[0].rule_id == "no-duplicate-edges"


# =========================================================================
# Rule: no-dangling-nodes
# =========================================================================


class TestNoDanglingNodes:
    def test_pass_all_connected(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("a", "nginx", "gateway", "edge"),
                _node("b", "fastapi", "compute", "application"),
            ],
            edges=[_edge("a", "b")],
        )
        issues = no_dangling_nodes.validate(design)
        assert issues == []

    def test_pass_single_node_no_edges(self) -> None:
        """Single-node designs are fine with no edges."""
        design = DesignDocument(
            nodes=[_node("a", "fastapi", "compute", "application")],
        )
        issues = no_dangling_nodes.validate(design)
        assert issues == []

    def test_fail_disconnected_node(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("a", "nginx", "gateway", "edge"),
                _node("b", "fastapi", "compute", "application"),
                _node("c", "redis", "cache", "data"),
            ],
            edges=[_edge("a", "b")],
        )
        issues = no_dangling_nodes.validate(design)
        assert len(issues) == 1
        assert issues[0].node_ids == ["c"]

    def test_fail_multiple_nodes_no_edges(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("a", "nginx", "gateway", "edge"),
                _node("b", "fastapi", "compute", "application"),
            ],
        )
        issues = no_dangling_nodes.validate(design)
        assert len(issues) == 2


# =========================================================================
# Rule: no-spof
# =========================================================================


class TestNoSpof:
    def test_pass_database_with_replicas(self) -> None:
        design = DesignDocument(
            nodes=[_node("db", "postgresql", "database", "data", replicas=3)],
        )
        issues = no_spof.validate(design)
        assert issues == []

    def test_pass_database_with_sibling(self) -> None:
        """Two databases in the design count as failover for each other."""
        design = DesignDocument(
            nodes=[
                _node("db1", "postgresql", "database", "data"),
                _node("db2", "postgresql-replica", "database", "data"),
            ],
        )
        issues = no_spof.validate(design)
        assert issues == []

    def test_fail_single_database(self) -> None:
        design = DesignDocument(
            nodes=[_node("db", "postgresql", "database", "data", replicas=1)],
        )
        issues = no_spof.validate(design)
        assert len(issues) == 1
        assert issues[0].rule_id == "no-spof"
        assert issues[0].severity == Severity.ERROR
        assert "db" in issues[0].node_ids

    def test_pass_compute_single_replica_ok(self) -> None:
        """Compute nodes are not flagged as SPOF by this rule."""
        design = DesignDocument(
            nodes=[_node("app", "fastapi", "compute", "application")],
        )
        issues = no_spof.validate(design)
        assert issues == []

    def test_fail_single_cache(self) -> None:
        design = DesignDocument(
            nodes=[_node("c", "redis", "cache", "data")],
        )
        issues = no_spof.validate(design)
        assert len(issues) == 1


# =========================================================================
# Rule: no-edge-to-db
# =========================================================================


class TestNoEdgeToDb:
    def test_pass_edge_to_app(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("cdn", "cloudflare", "cdn", "edge"),
                _node("app", "fastapi", "compute", "application"),
            ],
            edges=[_edge("cdn", "app")],
        )
        issues = no_edge_to_db.validate(design)
        assert issues == []

    def test_fail_edge_direct_to_db(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("cdn", "cloudflare", "cdn", "edge"),
                _node("db", "postgresql", "database", "data"),
            ],
            edges=[_edge("cdn", "db")],
        )
        issues = no_edge_to_db.validate(design)
        assert len(issues) == 1
        assert issues[0].rule_id == "no-edge-to-db"
        assert issues[0].severity == Severity.ERROR

    def test_fail_edge_to_cache(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("cdn", "cloudflare", "cdn", "edge"),
                _node("cache", "redis", "cache", "data"),
            ],
            edges=[_edge("cdn", "cache")],
        )
        issues = no_edge_to_db.validate(design)
        assert len(issues) == 1


# =========================================================================
# Rule: gateway-required
# =========================================================================


class TestGatewayRequired:
    def test_pass_gateway_present(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("gw", "kong", "gateway", "gateway"),
                _node("svc1", "users-svc", "compute", "application"),
                _node("svc2", "orders-svc", "compute", "application"),
            ],
        )
        issues = gateway_required.validate(design)
        assert issues == []

    def test_pass_single_app_service(self) -> None:
        """One app service doesn't require a gateway."""
        design = DesignDocument(
            nodes=[_node("app", "fastapi", "compute", "application")],
        )
        issues = gateway_required.validate(design)
        assert issues == []

    def test_fail_multiple_apps_no_gateway(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("svc1", "users-svc", "compute", "application"),
                _node("svc2", "orders-svc", "compute", "application"),
            ],
        )
        issues = gateway_required.validate(design)
        assert len(issues) == 1
        assert issues[0].rule_id == "gateway-required"
        assert issues[0].severity == Severity.WARNING


# =========================================================================
# Rule: cache-before-db
# =========================================================================


class TestCacheBeforeDb:
    def test_pass_cache_present(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("db", "postgresql", "database", "data"),
                _node("cache", "redis", "cache", "data"),
            ],
            requirements=DesignRequirements(expected_qps=5000),
        )
        issues = cache_before_db.validate(design)
        assert issues == []

    def test_pass_low_traffic(self) -> None:
        """Low traffic designs don't need cache."""
        design = DesignDocument(
            nodes=[_node("db", "postgresql", "database", "data")],
            requirements=DesignRequirements(expected_qps=500),
        )
        issues = cache_before_db.validate(design)
        assert issues == []

    def test_fail_high_qps_no_cache(self) -> None:
        design = DesignDocument(
            nodes=[_node("db", "postgresql", "database", "data")],
            requirements=DesignRequirements(expected_qps=2000),
        )
        issues = cache_before_db.validate(design)
        assert len(issues) == 1
        assert issues[0].rule_id == "cache-before-db"

    def test_fail_high_users_no_cache(self) -> None:
        design = DesignDocument(
            nodes=[_node("db", "postgresql", "database", "data")],
            requirements=DesignRequirements(expected_users=50000),
        )
        issues = cache_before_db.validate(design)
        assert len(issues) == 1


# =========================================================================
# Rule: async-for-heavy-writes
# =========================================================================


class TestAsyncProcessing:
    def test_pass_queue_present(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("app", "fastapi", "compute", "application"),
                _node("q", "rabbitmq", "queue", "async"),
            ],
            requirements=DesignRequirements(expected_qps=10000),
        )
        issues = async_processing.validate(design)
        assert issues == []

    def test_pass_low_qps(self) -> None:
        design = DesignDocument(
            nodes=[_node("app", "fastapi", "compute", "application")],
            requirements=DesignRequirements(expected_qps=1000),
        )
        issues = async_processing.validate(design)
        assert issues == []

    def test_fail_high_qps_no_async(self) -> None:
        design = DesignDocument(
            nodes=[_node("app", "fastapi", "compute", "application")],
            requirements=DesignRequirements(expected_qps=10000),
        )
        issues = async_processing.validate(design)
        assert len(issues) == 1
        assert issues[0].rule_id == "async-for-heavy-writes"


# =========================================================================
# Rule: data-store-required
# =========================================================================


class TestDataStoreRequired:
    def test_pass_database_present(self) -> None:
        design = DesignDocument(
            nodes=[_node("db", "postgresql", "database", "data")],
            requirements=DesignRequirements(data_durability_required=True),
        )
        issues = data_store_required.validate(design)
        assert issues == []

    def test_pass_storage_present(self) -> None:
        design = DesignDocument(
            nodes=[_node("s3", "aws-s3", "storage", "data")],
            requirements=DesignRequirements(data_durability_required=True),
        )
        issues = data_store_required.validate(design)
        assert issues == []

    def test_pass_durability_not_required(self) -> None:
        design = DesignDocument(
            nodes=[_node("app", "fastapi", "compute", "application")],
            requirements=DesignRequirements(data_durability_required=False),
        )
        issues = data_store_required.validate(design)
        assert issues == []

    def test_fail_no_store(self) -> None:
        design = DesignDocument(
            nodes=[_node("app", "fastapi", "compute", "application")],
            requirements=DesignRequirements(data_durability_required=True),
        )
        issues = data_store_required.validate(design)
        assert len(issues) == 1
        assert issues[0].rule_id == "data-store-required"
        assert issues[0].severity == Severity.ERROR


# =========================================================================
# Rule: multi-region-consistency
# =========================================================================


class TestMultiRegion:
    def test_pass_single_region(self) -> None:
        design = DesignDocument(
            nodes=[_node("db", "postgresql", "database", "data")],
            requirements=DesignRequirements(regions=1),
        )
        issues = multi_region.validate(design)
        assert issues == []

    def test_pass_enough_replicas(self) -> None:
        design = DesignDocument(
            nodes=[_node("db", "postgresql", "database", "data", replicas=3)],
            requirements=DesignRequirements(regions=3),
        )
        issues = multi_region.validate(design)
        assert issues == []

    def test_fail_insufficient_replicas(self) -> None:
        design = DesignDocument(
            nodes=[_node("db", "postgresql", "database", "data", replicas=1)],
            requirements=DesignRequirements(regions=3),
        )
        issues = multi_region.validate(design)
        assert len(issues) == 1
        assert issues[0].rule_id == "multi-region-consistency"


# =========================================================================
# Rule: throughput-bottleneck
# =========================================================================


class TestThroughputBottleneck:
    def test_pass_balanced_throughput(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("app", "fastapi", "compute", "application",
                      limits={"max_throughput_qps": 10000}),
                _node("db", "postgresql", "database", "data",
                      limits={"max_throughput_qps": 8000}),
            ],
            edges=[_edge("app", "db")],
        )
        issues = throughput_bottleneck.validate(design)
        assert issues == []

    def test_fail_severe_bottleneck(self) -> None:
        design = DesignDocument(
            nodes=[
                _node("app", "fastapi", "compute", "application",
                      limits={"max_throughput_qps": 50000}),
                _node("db", "postgresql", "database", "data",
                      limits={"max_throughput_qps": 5000}),
            ],
            edges=[_edge("app", "db")],
        )
        issues = throughput_bottleneck.validate(design)
        assert len(issues) == 1
        assert issues[0].rule_id == "throughput-bottleneck"

    def test_pass_no_limits_declared(self) -> None:
        """When limits are missing, no bottleneck is flagged."""
        design = DesignDocument(
            nodes=[
                _node("app", "fastapi", "compute", "application"),
                _node("db", "postgresql", "database", "data"),
            ],
            edges=[_edge("app", "db")],
        )
        issues = throughput_bottleneck.validate(design)
        assert issues == []


# =========================================================================
# Validator service (aggregation)
# =========================================================================


class TestValidatorService:
    def test_clean_design_passes(self) -> None:
        """A well-designed architecture should pass with zero errors."""
        design = DesignDocument(
            nodes=[
                _node("cdn", "cloudflare", "cdn", "edge"),
                _node("gw", "kong", "gateway", "gateway"),
                _node("app", "fastapi", "compute", "application",
                      limits={"max_throughput_qps": 20000}),
                _node("cache", "redis", "cache", "data", replicas=2),
                _node("db", "postgresql", "database", "data", replicas=3),
                _node("q", "rabbitmq", "queue", "async", replicas=2),
                _node("mon", "prometheus", "observability", "observability"),
            ],
            edges=[
                _edge("cdn", "gw"),
                _edge("gw", "app"),
                _edge("app", "cache"),
                _edge("app", "db"),
                _edge("app", "q"),
                _edge("app", "mon"),
            ],
            requirements=DesignRequirements(
                expected_qps=5000, expected_users=50000, regions=1
            ),
        )
        svc = ValidatorService()
        result = svc.validate(design)

        assert result.valid is True
        assert result.errors == 0
        assert len(result.rules_executed) == 12
        assert result.elapsed_ms < 1000  # must be fast

    def test_broken_design_has_errors(self) -> None:
        """A design with multiple issues should be flagged."""
        design = DesignDocument(
            nodes=[
                _node("cdn", "cloudflare", "cdn", "edge"),
                _node("db", "postgresql", "database", "data"),
            ],
            edges=[_edge("cdn", "db"), _edge("cdn", "db"), _edge("x", "y")],
            requirements=DesignRequirements(
                expected_qps=10000, data_durability_required=True
            ),
        )
        svc = ValidatorService()
        result = svc.validate(design)

        assert result.valid is False
        assert result.errors >= 2  # invalid-edge-refs + edge-to-db + spof
        assert result.total_issues >= 4

    def test_all_rules_registered(self) -> None:
        svc = ValidatorService()
        expected_rules = {
            "valid-edge-refs",
            "no-self-loops",
            "no-duplicate-edges",
            "no-dangling-nodes",
            "no-spof",
            "no-edge-to-db",
            "gateway-required",
            "cache-before-db",
            "async-for-heavy-writes",
            "data-store-required",
            "multi-region-consistency",
            "throughput-bottleneck",
        }
        assert set(svc.rule_ids) == expected_rules

    def test_performance_under_one_second(self) -> None:
        """Phase 3 definition of done: all rules run in under 1 second."""
        import time

        # Build a moderately large design
        nodes = []
        edges = []
        for i in range(100):
            nodes.append(
                _node(f"n{i}", f"svc-{i}", "compute", "application")
            )
        for i in range(99):
            edges.append(_edge(f"n{i}", f"n{i+1}"))

        design = DesignDocument(
            nodes=nodes,
            edges=edges,
            requirements=DesignRequirements(expected_qps=100000),
        )

        svc = ValidatorService()
        start = time.perf_counter()
        result = svc.validate(design)
        elapsed = time.perf_counter() - start

        assert elapsed < 1.0, f"Validation took {elapsed:.3f}s, must be < 1s"
        assert len(result.rules_executed) == 12


# =========================================================================
# API integration tests
# =========================================================================


@pytest.mark.asyncio
async def test_validate_endpoint(async_client: Any) -> None:
    """POST /api/v1/validator/validate returns correct result."""
    payload = {
        "nodes": [
            {
                "id": "app",
                "slug": "fastapi",
                "category": "compute",
                "layer": "application",
            },
            {
                "id": "db",
                "slug": "postgresql",
                "category": "database",
                "layer": "data",
                "replicas": 2,
            },
        ],
        "edges": [{"source_id": "app", "target_id": "db"}],
        "requirements": {"expected_qps": 100, "data_durability_required": True},
    }
    resp = await async_client.post("/api/v1/validator/validate", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "valid" in data
    assert "issues" in data
    assert "rules_executed" in data
    assert isinstance(data["rules_executed"], list)
    assert len(data["rules_executed"]) == 12


@pytest.mark.asyncio
async def test_list_rules_endpoint(async_client: Any) -> None:
    """GET /api/v1/validator/rules returns all rule IDs."""
    resp = await async_client.get("/api/v1/validator/rules")
    assert resp.status_code == 200
    data = resp.json()
    assert "rules" in data
    assert len(data["rules"]) == 12


@pytest.mark.asyncio
async def test_validate_empty_design_rejected(async_client: Any) -> None:
    """An empty nodes list should be rejected by Pydantic validation."""
    resp = await async_client.post(
        "/api/v1/validator/validate",
        json={"nodes": []},
    )
    assert resp.status_code == 422  # Pydantic validation error

