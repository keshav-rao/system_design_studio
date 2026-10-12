# Rules & Guidelines

## Working Agreement
1. Read the Memory Bank and relevant project doc before coding.
2. Implement only the current requested task; do not add unrequested features.
3. For changes touching more than two files, write a short plan and wait for approval.
4. Keep diffs small and reviewable; do not rewrite files unnecessarily.
5. Ask when requirements are ambiguous.
6. Update memory at the end of each task.

## Architecture Rules
- Catalog and validator are the source of truth, not the LLM.
- Parse every LLM response into Pydantic models; reject and retry invalid output.
- Put LLM, embedder, reranker, and vector store behind configurable interfaces.
- Validation rules are pure deterministic functions with unit tests.
- Keep routers thin: logic in services, data access in repositories.
- Every recommendation carries evidence IDs, assumptions, and alternatives.

## Backend Rules
- Python 3.11+, full type hints, async endpoints for I/O-bound work.
- Format with Ruff and Black; type-check with mypy.
- Use Pydantic v2 for request, response, and LLM schemas.
- Use Alembic for every database change.
- Read secrets and URLs from environment settings.
- Raise typed domain errors and convert to HTTP errors at the API layer.
- Use structured logging; do not log user content at info level by default.

## Frontend Rules
- Strict TypeScript; avoid `any` unless justified.
- Function components and hooks; keep components around 200 lines or less.
- TanStack Query for server state; Zustand or React state for local UI state.
- Generate API types from backend OpenAPI; do not hand-write API data types.
- Follow UI/UX tokens and make all interactive elements keyboard-accessible.

## Testing & Knowledge Rules
- Update tests with each change: unit tests for rules/services, API integration tests.
- Each validator rule needs a passing and failing test.
- Check retrieval changes against the eval set; never delete or weaken tests to pass.
- Ingest only sources with recorded licence or permission; no unauthorized copyrighted books.
- Date every source; refresh time-sensitive pricing, limits, and region facts.
