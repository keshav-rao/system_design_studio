# Rules and Memory Bank

## Working agreement
1. Read the Memory Bank and relevant project doc before coding.
2. Implement only the current requested task; do not add unrequested features.
3. For changes touching more than two files, write a short plan and wait for approval.
4. Keep diffs small and reviewable; do not rewrite files unnecessarily.
5. Ask when requirements are ambiguous.
6. Update memory at the end of each task.

## Architecture rules
- Catalog and validator are the source of truth, not the LLM.
- Parse every LLM response into Pydantic models; reject and retry invalid output.
- Put LLM, embedder, reranker, and vector store behind configurable interfaces.
- Validation rules are pure deterministic functions with unit tests.
- Keep routers thin: logic in services, data access in repositories.
- Every recommendation carries evidence IDs, assumptions, and alternatives.

## Backend rules
- Python 3.11+, full type hints, async endpoints for I/O-bound work.
- Format with Ruff and Black; type-check with mypy.
- Use Pydantic v2 for request, response, and LLM schemas.
- Use Alembic for every database change.
- Read secrets and URLs from environment settings.
- Raise typed domain errors and convert to HTTP errors at the API layer.
- Use structured logging; do not log user content at info level by default.

## Frontend rules
- Strict TypeScript; avoid `any` unless justified.
- Function components and hooks; keep components around 200 lines or less.
- TanStack Query for server state; Zustand or React state for local UI state.
- Generate API types from backend OpenAPI; do not hand-write API data types.
- Follow UI/UX tokens and make all interactive elements keyboard-accessible.

## Testing and knowledge rules
- Update tests with each change: unit tests for rules/services, API integration tests, and a few core-flow E2E tests.
- Each validator rule needs a passing and failing test.
- Check retrieval changes against the eval set; never delete or weaken tests to pass.
- Ingest only sources with recorded licence or permission; no unauthorized copyrighted books.
- Date every source; refresh time-sensitive pricing, limits, and region facts.

## Git and safety
- Use Conventional Commit prefixes (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`).
- Use one branch per task; do not commit directly to `main`.
- Do not destructively alter databases, force-push, or delete volumes without explicit confirmation.
- Before adding a dependency, explain why and list alternatives.

## Project Memory Bank

### projectBrief
- Name: AI System Design Architect.
- Purpose: turn app ideas into validated, evidence-backed system architectures.
- Core approach: RAG + DeepSeek-R1 + structured catalog + deterministic validator; fine-tuning only after measured failures.
- Users: solo developers, startup engineers, interview candidates.
- Open-source; use only permitted knowledge sources.

### productContext
Generic chatbots are unsourced and unchecked. UX prioritizes evidence on every claim, an editable canvas, and visible validation. Example: dating app with profiles, matching, image uploads, and real-time chat.

### techContext
FastAPI, Pydantic v2, PostgreSQL, Qdrant, bge-m3, bge-reranker-v2-m3, LlamaIndex, DeepSeek-R1-Distill-Qwen-32B, React, TypeScript, React Flow, Docker Compose. Candidate models remain provisional until evaluated. The system runs locally, with model/embedder/reranker swappable by configuration.

### systemPatterns
Pipeline: ingest → chunk → metadata → embed → index → hybrid retrieve → rerank → plan → validate → canvas. Validate planner output against schema and retry at most twice. Catalog owns component compatibility and limits. Designs are append-only; partial re-plan touches affected nodes. Layering: router → service → repository, with adapters for external/model services.

### activeContext template
```text
Current phase: Phase 0 — Foundation
Current task: set up repo and Docker Compose
Last completed: nothing yet
In progress: —
Next up: FastAPI skeleton and health endpoint
Open questions: LlamaIndex vs LangChain (default LlamaIndex); vLLM vs Ollama
Blockers: none
```

### progress template
```markdown
## Done
- (none yet)

## In progress
- Phase 0

## Upcoming
- Phase 1 knowledge base → Phase 2 catalog → Phase 3 validator → Phase 4 planner → Phase 5 canvas → Phase 6 iteration → Phase 7 evaluation

## Known issues
- (none yet)
```

### decisionLog starter decisions
- RAG before fine-tuning: knowledge changes and needs citations; fine-tune only after failure analysis.
- Structured catalog alongside vector search: improves control and provides hard facts for validation.
- Deterministic validator: model output is never trusted without checks.
- Choose one orchestration framework to avoid complexity (default LlamaIndex).
- Treat embedder and reranker as candidates; evaluate on project questions.

### evalNotes
Track latest run date, configuration, recall@k, MRR, schema validity, validator pass rate, citation correctness, failure categories, and next experiments.

### Memory maintenance
Update active context and progress after every task. Record technical choices in decisionLog. Keep each memory file to about one screen, summarizing older items. When asked to update the Memory Bank, review and correct stale entries.
