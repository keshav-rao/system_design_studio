Run cmd

docker compose up -d --build

npm --prefix frontend run dev -- --host 0.0.0.0


Frontend UI: http://localhost:3000
Backend API & Swagger Docs: http://localhost:8000/docs
Qdrant Vector DB Dashboard: http://localhost:6333/dashboard
PostgreSQL: localhost:5432

# Run backend
docker run -d --name sd-backend -p 8000:8000 system-design-backend:latest
# Run frontend
docker run -d --name sd-frontend -p 3000:80 system-design-frontend:latest


Running Services Status
Service	Container Name	Health / Status	Port / URL
Frontend UI	system_design_frontend	Up (Healthy)	http://localhost:3000
Backend API & Swagger	system_design_backend	Up (Healthy)	http://localhost:8000/docs
PostgreSQL 16	system_design_postgres	Up (Healthy)	localhost:5432
Qdrant Vector DB	system_design_qdrant	Up (Running)	http://localhost:6333/dashboard

## RAG corpus ingestion (LlamaIndex + bge-m3)

Everything under `rag_knowledge_base/` is the authoritative corpus. LlamaIndex reads and chunks it, `BAAI/bge-m3` produces dense and sparse vectors in one pass, Qdrant does hybrid RRF search, and `BAAI/bge-reranker-v2-m3` reranks the results.

```bash
cd backend
python -m app.cli.ingest_corpus --recreate --eval   # first run / model change
python -m app.cli.ingest_corpus                     # incremental: only changed files
python -m app.cli.ingest_corpus --collections 03_component_decision_guides
```

Set `EMBEDDING_PROVIDER=hash` and `RERANKER_PROVIDER=lexical` for offline/CPU-only development. A full-corpus bge-m3 ingest needs a GPU; on CPU it takes many hours.
