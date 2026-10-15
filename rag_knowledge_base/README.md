# RAG Knowledge Base — System Design Studio

This directory contains the curated, traceable raw materials and structured knowledge documents for the System Design Studio RAG (Retrieval-Augmented Generation) engine.

## Knowledge Base Architecture

```
rag_knowledge_base/
├── README.md                                  # Knowledge base architecture, guidelines, and ingestion rules
├── corpus_manifest.json                       # Machine-readable catalog of all documents with metadata
├── 01_fundamentals/                           # Core distributed systems theory and design principles
│   ├── cap_and_pacelc_theorem.md
│   ├── consistency_models_and_isolation.md
│   ├── replication_and_partitioning.md
│   ├── horizontal_vs_vertical_scaling.md
│   ├── availability_and_fault_tolerance.md
│   └── caching_principles_and_invalidation.md
├── 02_cloud_frameworks/                       # Cloud-native reference frameworks
│   ├── aws_well_architected_framework.md
│   ├── gcp_architecture_framework.md
│   ├── azure_architecture_center.md
│   └── system_design_primer_reference.md
├── 03_component_decision_guides/              # Technology selection & trade-off guides
│   ├── caching_redis_vs_memcached.md
│   ├── event_streaming_kafka_vs_rabbitmq.md
│   ├── relational_databases_postgresql.md
│   ├── nosql_databases_mongodb_cassandra_dynamo.md
│   ├── traffic_management_dns_cdn_load_balancers.md
│   ├── container_orchestration_kubernetes.md
│   └── object_storage_and_s3_patterns.md
├── 04_reference_architectures/                # Production architectures with trade-offs
│   ├── tinder_dating_app_architecture.md
│   ├── whatsapp_realtime_chat_architecture.md
│   ├── netflix_video_streaming_architecture.md
│   ├── uber_ride_hailing_geospatial.md
│   ├── amazon_ecommerce_and_inventory.md
│   └── notification_system_multi_channel.md
├── 05_performance_and_load_testing/           # Workload modeling & benchmark data
│   ├── k6_and_locust_load_testing_guide.md
│   ├── latency_percentiles_and_sla_slo_sli.md
│   ├── database_limits_and_connection_pooling.md
│   └── failure_modes_circuit_breaking_thundering_herd.md
├── 06_cost_and_capacity_models/               # Cost calculation models & capacity sizing
│   ├── back_of_the_envelope_estimation_rules.md
│   ├── cloud_pricing_records_and_calculator_models.md
│   └── storage_compute_bandwidth_sizing.md
└── 07_architecture_decision_records/          # Formal Architecture Decision Records (ADRs)
    ├── adr_001_sql_vs_nosql_selection.md
    ├── adr_002_kafka_vs_rabbitmq_event_broker.md
    ├── adr_003_redis_in_memory_data_store.md
    ├── adr_004_layer_4_vs_layer_7_load_balancer.md
    └── adr_005_monolith_vs_microservices_vs_serverless.md
```

## Metadata Standard

Every document begins with a strict JSON metadata block:
```json
{
  "topic": "<topic_category>",
  "component": "<component_name_or_neutral>",
  "decision_type": "<technology_selection|capacity_planning|failure_mitigation|pattern_design>",
  "content_type": "<official_documentation|reference_architecture|benchmark|adr>",
  "cloud_provider": "<provider_neutral|aws|gcp|azure>",
  "source_url": "<official_canonical_url>",
  "version": "<documented_version>",
  "licence": "<CC-BY-4.0|Apache-2.0|MIT|Open-Documentation>",
  "last_verified": "2026-10-14"
}
```

## Three-Tier Grounding Rule

1. **RAG Knowledge Base**: Conceptual reasoning, architectural trade-offs, edge cases, and rationale.
2. **Structured Component Catalog**: Machine-validated JSON/SQL component definitions with exact connection constraints.
3. **Deterministic Engineering Tools**: Quantitative capacity calculations, cost simulation formulas, and network rule validator.
