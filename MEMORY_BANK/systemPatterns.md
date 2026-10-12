# System Patterns

## Data Flow Pipeline
```
[User App Idea]
      │
      ▼
[Requirements Interview (Adaptive questioning: QPS, DB, Cache, LB, Queues)]
      │
      ▼
[Hybrid Knowledge Retrieval (Dense + Sparse in Qdrant)]
      │
      ▼
[Architecture Proposal Generator (Grounding in Catalog Facts & Evidence)]
      │
      ▼
[Deterministic Validator (Interface checks, SPOF, limits, requirements)]
      │
      ▼
[Interactive React Flow Canvas (Layered nodes, rationale, tool selection)]
      │
      ▼
[Capacity & Load Simulation (1 / 100 / 1k / 100k users)]
      │
      ▼
[Cost Matrix & Tiered Estimates (Free vs Pro cloud breakdown)]
```

## Architectural Guidelines
- **Catalog as Truth**: Components slug, interface compatibility, failure modes, and cost units must be catalog-backed.
- **Append-only Design Snapshots**: Every canvas modification produces a traceable design version.
- **Pure Function Validators**: Validation rules are deterministic, fast (<1s), and unit-tested with both passing and failing scenarios.
- **Layering**: Routers -> Services -> Repositories -> Models.
