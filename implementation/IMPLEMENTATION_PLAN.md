# Implementation Plan

Build in vertical slices. Finish and test each phase before starting the next.

## Phase 0: Foundation (days 1–3)
- Create `backend/`, `frontend/`, `docs/`, and `docker-compose.yml`.
- Add FastAPI skeleton, environment-based config, health endpoint, and Pydantic settings.
- Compose PostgreSQL and Qdrant; set up Alembic.
- Add Rules and Memory Bank files at repo root.
- Done when Compose starts services and `/health` returns OK.

## Phase 1: Knowledge base (week 1–2)
- Ingest Markdown and PDF first; add DOCX and HTML later.
- Build heading-aware chunking with collection, source, licence, and date metadata.
- Embed with bge-m3 and index in Qdrant with dense and sparse vectors.
- Add ingest/search endpoints and filters; make reranker configurable.
- Seed 20–30 permitted documents across five collections.
- Done when search returns relevant cited chunks for 10 hand-written questions.

## Phase 2: Structured component catalog (week 2–3)
- Add catalog tables and seed 30–50 components (CDN, object storage, cache, relational DB, queue, WebSocket gateway, API gateway, auth, search, notifications, etc.).
- Add compatibility edges, limits, failure modes, and cost units.
- Add read API and simple admin form.
- Done when the catalog can answer whether A connects to B and which limits apply.

## Phase 3: Validator (week 3–4)
- Implement each rule as a small pure function, one file per rule.
- Test every rule with passing and failing designs.
- Add project validation endpoint.
- Done when all initial rules have tests and run in under one second.

## Phase 4: Planner (week 4–5)
- Add LLM adapter interface and DeepSeek-R1-Distill-Qwen-32B implementation via vLLM or Ollama.
- Start with a fixed requirements interview, then add adaptive follow-ups.
- Prompt with requirements, retrieved evidence, and catalog facts; require `ArchitectureProposal` output.
- Parse with Pydantic, retry invalid output at most twice, then run validator.
- Store design version, evidence links, and issues.
- Done when the dating-app example yields a schema-valid design that passes validation or reports clear issues.

## Phase 5: Frontend canvas (week 5–7)
- Build Vite + React + TypeScript + Tailwind and generate API client from OpenAPI.
- Implement interview, requirements review, and React Flow canvas.
- Add Component, Validation, Evidence, and Cost tabs.
- Support add/remove/replace component and compatibility-checked connections.
- Done when users can go from idea to edited, validated diagram in the UI.

## Phase 6: Iterative redesign (week 7–8)
- Detect nodes affected by a requirement or component change.
- Re-retrieve and re-plan only that subgraph; show a version diff.
- Added a versioned redesign endpoint that infers affected nodes from changed requirements or accepts explicit node IDs, then grounds planning in the existing subgraph and its boundaries.
- Merge the generated subgraph with untouched nodes and edges, validate the complete result, and persist a new immutable design version.
- The canvas supports focused redesign, NFR edits, and a before/after node, connection, and requirement diff.
- Done when changing the database or user count updates only relevant parts. ✅

## Phase 7: Evaluation and hardening (week 8–9)
- Build an eval set of 100+ questions and 15+ gold designs with a runner.
- Compare embedder, reranker, chunk size, and prompt variants.
- Add logging, tracing, rate limits, and error pages.
- Write README, setup guide, and contribution guide.
- Done when PRD metrics are measured and documented.

## Phase 8: Optional fine-tuning
Only after categorizing failures as missing knowledge, poor retrieval, wrong reasoning, bad requirements, or invalid generation. Fine-tune only behavior issues such as planning style, requirement questioning, or schema adherence, and compare to the RAG baseline on the same eval set.

## Definition of done
Tests pass, types and linters are clean, no secrets are committed, Memory Bank is updated, and behavior-changing docs are updated.
