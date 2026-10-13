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

### Planned Endpoints (Phases 2-6)
- `POST /projects`: Create a new architecture project.
- `POST /projects/{id}/interview`: Interactive requirement questioning.
- `POST /projects/{id}/plan`: Generate proposal with planner.
- `POST /projects/{id}/validate`: Run deterministic validation rules.
- `PATCH /projects/{id}/design`: Update nodes/edges from canvas edits.
- `GET /catalog/components`: Retrieve component catalog with alternatives & limits.
