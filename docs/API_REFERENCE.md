# API Reference

## Base URLs
- Local Development: `http://localhost:8000`
- API Version 1 Prefix: `/api/v1`

## Endpoints

### Health & Diagnostics
- `GET /health`
  - Returns basic application health, name, version, and environment.
  - Response:
    ```json
    {
      "status": "ok",
      "app": "System Design Studio",
      "version": "0.1.0",
      "environment": "development"
    }
    ```
- `GET /api/v1/health`
  - Alias for health check.
- `GET /api/v1/health/ready`
  - Readiness check probing PostgreSQL database and Qdrant vector store.
  - Response:
    ```json
    {
      "status": "ok",
      "checks": {
        "database": "healthy",
        "qdrant": "healthy"
      }
    }
    ```

### Knowledge Base (Phase 1)
- `POST /api/v1/knowledge/ingest`
  - Ingests structured document content into PostgreSQL and indexes heading-aware chunks into Qdrant with dense and sparse vectors.
  - Body:
    ```json
    {
      "title": "Consistent Hashing and Virtual Nodes",
      "collection": "foundations",
      "content": "# Consistent Hashing\n...",
      "licence": "CC-BY-4.0",
      "publication_date": "2024-01-01",
      "tags": ["distributed", "hashing"]
    }
    ```
- `POST /api/v1/knowledge/upload`
  - Multipart file upload supporting Markdown (`.md`) and PDF (`.pdf`) documents.
- `POST /api/v1/knowledge/search`
  - Hybrid dense (bge-m3) and sparse (BM25) vector retrieval with payload filtering and configurable reranking.
  - Body:
    ```json
    {
      "query": "how to detect mutual match in tinder",
      "limit": 5,
      "use_reranker": true,
      "filter": {
        "collections": ["case_studies"]
      }
    }
    ```
- `GET /api/v1/knowledge/sources`
  - Lists ingested sources with optional `collection` query filter.
- `GET /api/v1/knowledge/sources/{id}`
  - Returns metadata and chunk counts for a specific source.
- `POST /api/v1/knowledge/seed`
  - Seeds 25 verified reference documents across 5 collections (`foundations`, `patterns`, `cloud_docs`, `capacity`, `case_studies`).
- `POST /api/v1/knowledge/eval`
  - Runs retrieval quality benchmark against 10 hand-written system design evaluation questions. Computes MRR, Recall@3, and Recall@5.

### Structured Component Catalog (Phase 2)
- `GET /api/v1/catalog/components`
  - Lists architectural components with optional filters: `category`, `layer`, `search`, `limit`, `offset`.
  - Response:
    ```json
    {
      "total": 41,
      "items": [
        {
          "id": "...",
          "slug": "postgresql",
          "name": "PostgreSQL Relational Database",
          "category": "database",
          "layer": "data",
          "description": "Advanced ACID-compliant object-relational SQL database...",
          "protocols": ["TCP", "SQL"],
          "limits": {
            "max_throughput_qps": 20000,
            "connection_limit": 500,
            "latency_p99_ms": 15
          },
          "failure_modes": [...],
          "cost_units": {
            "model": "provisioned",
            "base_monthly_usd": 30.0
          },
          "alternatives": ["mysql", "cockroachdb"]
        }
      ]
    }
    ```
- `GET /api/v1/catalog/components/{slug_or_id}`
  - Retrieves detailed component specifications, limits, failure modes, cost units, and alternatives by slug or UUID.
- `POST /api/v1/catalog/components`
  - Registers a new architectural building block into the catalog.
- `PUT /api/v1/catalog/components/{id}`
  - Updates an existing component's specs, limits, or metadata.
- `DELETE /api/v1/catalog/components/{id}`
  - Removes a component from the catalog.
- `GET /api/v1/catalog/compatibility/check`
  - Determines whether Component A can interface with Component B, identifying communication protocols, recommended architectural patterns (e.g., PgBouncer pooling, cache-aside), bottleneck throughput limits, and antipattern warnings.
  - Query parameters: `source`, `target` (e.g. `?source=fastapi-app-server&target=postgresql`).
- `POST /api/v1/catalog/compatibility`
  - Defines or updates a compatibility edge between two components.
- `POST /api/v1/catalog/seed`
  - Seeds or resets 40+ standard architectural components and 30+ compatibility rules idempotently.

### Projects & Planner (Phases 4-6)
- `POST /projects`: Create a new architecture project.
- `GET /api/v1/projects`: List architecture projects.
- `POST /api/v1/projects/interview`: Interactive requirement questioning.
- `POST /api/v1/projects/{id}/plan`: Generate and persist a complete design version.
- `POST /api/v1/projects/{id}/redesign`: Re-plan only affected nodes and their local connections, merge with unchanged parts, validate, and persist a new design version.
  - Body includes `change_description`, the full updated `requirements`, and optional `affected_node_ids`. If no node is selected, changed requirement fields and change-description terms are used to infer affected components.
  - Returns the new version. Compare it with the previous version to inspect added, removed, or updated components and connections.
- `GET /api/v1/projects/{id}/designs`: List version history.
- `GET /api/v1/projects/{id}/designs/latest`: Get the current version.
