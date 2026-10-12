# Technical Requirements

## System overview
Knowledge sources flow through extraction, chunking, metadata enrichment, embedding, and indexing. User requirements pass through an interview; the planner receives retrieved evidence and catalog facts, produces a proposal, and hands it to the deterministic validator before the canvas. Canvas edits trigger retrieval and planning for affected areas.

## Candidate stack
| Layer | Choice | Notes |
|---|---|---|
| Backend | Python 3.11+, FastAPI, Pydantic v2 | Typed requests, responses, and planner output |
| Ingestion | PyMuPDF, python-docx, HTML/Markdown parsers | Parser per format |
| Chunking | Custom Python pipeline | Heading-aware chunks with metadata |
| Embeddings | BAAI/bge-m3 | Candidate; evaluate on project questions |
| Vector DB | Qdrant | Dense plus sparse hybrid search |
| Reranker | BAAI/bge-reranker-v2-m3 | Candidate; rerank top 30 to top 6 |
| Orchestration | LlamaIndex or LangChain | Default LlamaIndex; choose one |
| LLM | DeepSeek-R1-Distill-Qwen-32B | Serve through vLLM or Ollama adapter |
| Relational DB | PostgreSQL | Catalog, projects, designs, evaluations |
| Frontend | React, TypeScript, React Flow, Tailwind | Canvas and side panels |
| Infra | Docker Compose | API, Qdrant, PostgreSQL, LLM server, web |

All model, embedder, reranker, and vector-store implementations must be swappable through configuration.

## Functional requirements
- FR1: Ingest PDF, DOCX, HTML, and Markdown with collection, source, licence, date, version, and tags.
- FR2: Search returns chunks with scores, source, and citation metadata.
- FR3: Catalog API returns components, compatibility edges, and limits.
- FR4: Planner accepts requirements, evidence, and catalog facts; returns `ArchitectureProposal`. Invalid JSON receives a bounded retry.
- FR5: Validator returns issues with severity, location, and suggested fix.
- FR6: Partial re-plan recomputes only components affected by a change.
- FR7: Every recommendation stores evidence IDs, assumptions, and alternatives.

## Non-functional requirements
- Validation is deterministic: identical designs produce identical results.
- Planner output is schema-validated before use.
- Long planner runs support streaming.
- Log retrieval queries, selected chunks, prompts, outputs, and validator results per run.
- Run locally/offline with open-source models.

## Initial validation rules
- Connections must match an allowed catalog interface pair.
- No orphan components; every requirement maps to one or more components.
- Public entry points require auth or access control.
- Stateful components require backup or replication strategy.
- Flag single points of failure when availability target exceeds 99.9%.
- Check estimated QPS, storage, and connections against catalog limits.
- Image upload flows require object storage, processing, and delivery such as a CDN.
- Real-time features require a connection layer (for example WebSockets) and fan-out strategy.

## API endpoints
- `POST /projects`, `GET /projects/{id}`
- `POST /projects/{id}/interview`
- `POST /projects/{id}/plan` (streaming supported)
- `POST /projects/{id}/validate`
- `PATCH /projects/{id}/design`
- `GET /catalog/components`, `GET /catalog/components/{id}`
- `POST /knowledge/ingest`, `POST /knowledge/search`

## Evaluation
Maintain questions and gold designs. Measure retrieval quality, schema validity, validator pass rate, citation correctness, and human ratings. Run evaluations after changes to prompts, chunking, embeddings, or models.
