"""Deterministic Mock adapter for testing and offline development."""

import json
from typing import Any

from app.services.planner.providers.base import BaseLLMAdapter


class MockLLMAdapter(BaseLLMAdapter):
    """Generates schema-valid ArchitectureProposal JSON deterministically."""

    def __init__(self, fail_first_n_times: int = 0) -> None:
        self.fail_first_n_times = fail_first_n_times
        self._call_count = 0

    async def is_available(self) -> bool:
        return True

    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        temperature: float = 0.2,
    ) -> str:
        self._call_count += 1
        if self._call_count <= self.fail_first_n_times:
            # Return invalid JSON to simulate LLM formatting failure for retry testing
            return (
                "Thinking... [Broken output without closing bracket: { 'title': 'Draft'"
            )

        prompt_lower = prompt.lower()
        if (
            "tinder" in prompt_lower
            or "dating" in prompt_lower
            or "match" in prompt_lower
        ):
            return json.dumps(self._build_dating_app_proposal(), indent=2)

        return json.dumps(self._build_generic_proposal(), indent=2)

    def _build_dating_app_proposal(self) -> dict[str, Any]:
        """Golden proposal for the dating-app example required by Phase 4."""
        return {
            "title": "Tinder-Scale Real-Time Geospatial & Mutual Matching Architecture",
            "summary": (
                "A distributed, low-latency architecture for high-concurrency swipe matching. "
                "Traffic enters via Cloudflare CDN and Kong API Gateway, terminating TLS and routing "
                "to FastAPI application servers. Active user locations and mutual swipe candidate sets "
                "are indexed in an in-memory Redis cluster with Geospatial indexing and bitsets. "
                "High-volume swipe events are buffered asynchronously through RabbitMQ for worker processing. "
                "User profiles and match records are durably persisted across partitioned PostgreSQL instances."
            ),
            "nodes": [
                {
                    "id": "edge_cdn",
                    "slug": "cloudflare",
                    "category": "cdn",
                    "layer": "edge",
                    "replicas": 3,
                    "protocols": ["HTTPS"],
                    "limits": {"max_throughput_qps": 100000},
                },
                {
                    "id": "gw",
                    "slug": "kong-gateway",
                    "category": "gateway",
                    "layer": "gateway",
                    "replicas": 2,
                    "protocols": ["HTTPS", "WSS", "HTTP"],
                    "limits": {"max_throughput_qps": 50000},
                },
                {
                    "id": "app_match",
                    "slug": "fastapi",
                    "category": "compute",
                    "layer": "application",
                    "replicas": 4,
                    "protocols": ["HTTP", "TCP"],
                    "limits": {"max_throughput_qps": 20000},
                },
                {
                    "id": "cache_geo",
                    "slug": "redis-cache",
                    "category": "cache",
                    "layer": "data",
                    "replicas": 2,
                    "protocols": ["RESP", "TCP"],
                    "limits": {"max_throughput_qps": 100000},
                },
                {
                    "id": "queue_swipes",
                    "slug": "rabbitmq",
                    "category": "queue",
                    "layer": "async",
                    "replicas": 2,
                    "protocols": ["AMQP", "TCP"],
                    "limits": {"max_throughput_qps": 30000},
                },
                {
                    "id": "db_primary",
                    "slug": "postgresql",
                    "category": "database",
                    "layer": "data",
                    "replicas": 2,
                    "protocols": ["SQL", "TCP"],
                    "limits": {"max_throughput_qps": 15000},
                },
            ],
            "edges": [
                {
                    "source_id": "edge_cdn",
                    "target_id": "gw",
                    "protocol": "HTTPS",
                    "label": "Edge routing",
                },
                {
                    "source_id": "gw",
                    "target_id": "app_match",
                    "protocol": "HTTP",
                    "label": "Reverse proxy",
                },
                {
                    "source_id": "app_match",
                    "target_id": "cache_geo",
                    "protocol": "RESP",
                    "label": "Sub-ms Geo & Cache query",
                },
                {
                    "source_id": "app_match",
                    "target_id": "queue_swipes",
                    "protocol": "AMQP",
                    "label": "Async swipe event buffer",
                },
                {
                    "source_id": "app_match",
                    "target_id": "db_primary",
                    "protocol": "SQL",
                    "label": "Durable profile persistence",
                },
            ],
            "requirements": {
                "expected_users": 100000,
                "expected_qps": 5000,
                "availability_target": 99.95,
                "data_durability_required": True,
                "regions": 1,
            },
            "assumptions": [
                "Peak swipe activity is 5,000 QPS with 80% read (profile discovery) to 20% write (swipes).",
                "User proximity queries use Redis GeoRadius or H3 hexagonal cell indexing for sub-5ms responses.",
                "Mutual match detection uses Redis Sets/Bitsets (intersection check) before queuing notification tasks.",
            ],
            "evidence_links": [
                {
                    "source_id": None,
                    "source_title": "Tinder System Architecture & Redis Matching Strategy",
                    "collection": "case_studies",
                    "section_path": "# Tinder Architecture > ## Mutual Match Algorithm",
                    "snippet": "Tinder uses in-memory Redis clusters with geospatial indexing and Set intersections to evaluate reciprocal right-swipes in sub-millisecond latency.",
                    "relevance_score": 0.94,
                },
                {
                    "source_id": None,
                    "source_title": "Caching Architecture Patterns",
                    "collection": "patterns",
                    "section_path": "# Cache-Aside & Write-Back > ## High Throughput Scaling",
                    "snippet": "Under high read-to-write ratios exceeding 1,000 QPS, place an in-memory caching tier in front of relational databases to protect connection pools.",
                    "relevance_score": 0.89,
                },
            ],
            "alternatives_considered": [
                {
                    "component_slug": "rabbitmq",
                    "considered_against": "kafka",
                    "rationale": "RabbitMQ chosen for flexible message routing and lightweight consumer acknowledgments without partition-rebalance overhead.",
                },
                {
                    "component_slug": "redis-cache",
                    "considered_against": "memcached",
                    "rationale": "Redis selected because it natively supports geospatial indices (GEOADD, GEORADIUS) and Set operations required for instant mutual match detection.",
                },
            ],
        }

    def _build_generic_proposal(self) -> dict[str, Any]:
        """Generic web app proposal."""
        return {
            "title": "Scalable Three-Tier Web Architecture",
            "summary": "Three-tier architecture with Kong API Gateway, FastAPI compute, Redis cache, and PostgreSQL database.",
            "nodes": [
                {
                    "id": "gw",
                    "slug": "kong-gateway",
                    "category": "gateway",
                    "layer": "gateway",
                    "replicas": 2,
                    "protocols": ["HTTPS", "HTTP"],
                    "limits": {"max_throughput_qps": 50000},
                },
                {
                    "id": "app",
                    "slug": "fastapi",
                    "category": "compute",
                    "layer": "application",
                    "replicas": 2,
                    "protocols": ["HTTP", "TCP"],
                    "limits": {"max_throughput_qps": 10000},
                },
                {
                    "id": "cache",
                    "slug": "redis-cache",
                    "category": "cache",
                    "layer": "data",
                    "replicas": 2,
                    "protocols": ["RESP", "TCP"],
                    "limits": {"max_throughput_qps": 50000},
                },
                {
                    "id": "db",
                    "slug": "postgresql",
                    "category": "database",
                    "layer": "data",
                    "replicas": 2,
                    "protocols": ["SQL", "TCP"],
                    "limits": {"max_throughput_qps": 10000},
                },
            ],
            "edges": [
                {
                    "source_id": "gw",
                    "target_id": "app",
                    "protocol": "HTTP",
                    "label": "Routing",
                },
                {
                    "source_id": "app",
                    "target_id": "cache",
                    "protocol": "RESP",
                    "label": "Cache query",
                },
                {
                    "source_id": "app",
                    "target_id": "db",
                    "protocol": "SQL",
                    "label": "Persistence",
                },
            ],
            "requirements": {
                "expected_users": 10000,
                "expected_qps": 1000,
                "availability_target": 99.9,
                "data_durability_required": True,
                "regions": 1,
            },
            "assumptions": [
                "Standard CRUD web workload with read-heavy cache utilization."
            ],
            "evidence_links": [],
            "alternatives_considered": [],
        }
