# Decision Log

## Initial Decisions (Phase 0)
1. **RAG before fine-tuning**: Architecture rules and cloud pricing evolve rapidly; citations and evidence retrieval provide transparency, while fine-tuning is deferred until evaluation demonstrates specific behavioral shortcomings.
2. **Structured Component Catalog**: Catalog serves as hard ground truth for allowed connections, interface matching, scaling limits, and tool alternatives (e.g., Redis vs AWS ElastiCache, Nginx vs ALB).
3. **Deterministic Validator**: Architectures must pass programmatic checks; generative model output is never presented without deterministic validation.
4. **Async SQLAlchemy + AsyncPG**: Non-blocking async database layer with Alembic async migrations for PostgreSQL.
5. **FastAPI + Pydantic v2**: High performance, strict type safety, automatic OpenAPI docs generation.
6. **Dual Health Probing**: Lightweight liveness probe (`/health`) and comprehensive readiness probe (`/api/v1/health/ready`) checking DB and Qdrant connectivity.
