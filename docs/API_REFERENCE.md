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

### Planned Endpoints (Phases 1-6)
- `POST /projects`: Create a new architecture project.
- `POST /projects/{id}/interview`: Interactive requirement questioning.
- `POST /projects/{id}/plan`: Generate proposal with planner.
- `POST /projects/{id}/validate`: Run deterministic validation rules.
- `PATCH /projects/{id}/design`: Update nodes/edges from canvas edits.
- `GET /catalog/components`: Retrieve component catalog with alternatives & limits.
- `POST /knowledge/search`: Hybrid search over knowledge chunks.
