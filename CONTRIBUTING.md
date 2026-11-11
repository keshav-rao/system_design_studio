# Contributing

Thanks for helping improve System Design Studio. Keep changes focused, evidence-backed, and testable. Read [RULES.md](RULES.md) and [ARCHITECTURE.md](ARCHITECTURE.md) before changing architecture or RAG behavior.

## Branches and commits

- Branch from the current default branch using a short kebab-case name such as `feat/notion-loader` or `fix/chunk-metadata`.
- Keep commits focused and use imperative subjects, for example `Add source metadata to search results`.
- Do not commit credentials, private datasets, generated vector indexes, local model weights, or unlicensed corpus content.
- Open a pull request for review; do not merge changes that have failing required checks or unresolved data-rights questions.

## Local development

Start dependencies with `docker compose up -d postgres qdrant`. Configure `.env` from `.env.example`, then create a Python 3.11+ virtual environment and install backend dependencies:

```bash
cd backend
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
alembic upgrade head
```

Run the API with `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`. Run the frontend with `npm --prefix frontend install` and `npm --prefix frontend run dev -- --host 0.0.0.0`.

## Code quality and tests

Backend Python targets 3.11 and uses 88-character lines. Run checks from `backend/`:

```bash
pytest
ruff check .
black --check .
mypy app
```

Format changed files with Ruff/Black according to the existing `pyproject.toml`. Use full type hints, Pydantic v2 for API/planner contracts, async I/O for I/O-bound endpoints, and Alembic for schema changes. Keep routers thin; put business behavior in services, persistence access in repositories, and provider-specific logic behind interfaces.

For frontend changes, use strict TypeScript and run `npm --prefix frontend run build` from the repository root. Add or update tests alongside behavior changes. Validator rules require passing and failing cases. Retrieval changes require an evaluation against the maintained benchmark; do not weaken or remove tests to make a change pass.

## Naming conventions

- Python files and packages: `snake_case` (`heading_aware_chunker.py`).
- Root documentation: `UPPER_SNAKE_CASE.md`, with conventional `README.md` retained.
- Configuration and infrastructure directories: kebab-case (`model-serving/`).
- Tests: `test_<module>.py` with behavior-oriented test names.
- Loaders/connectors: `<source>_loader.py`; chunkers: `<strategy>_chunker.py`; retrievers: `<strategy>_retriever.py`.
- Classes use CapWords and clear role names, such as `MarkdownLoader` or `HybridRetriever`.

## Adding a data connector

1. Confirm the source is permitted for ingestion. Record its origin, licence or permission basis, publication date, version/refresh date, and any handling restrictions. Do not ingest copyrighted content without authorization.
2. Add a focused snake_case loader module under the knowledge ingestion area. Keep network/source-specific fetching separate from parsing and chunking so local files can be tested without credentials.
3. Normalize connector output into the existing document/chunk metadata contract. Preserve a stable source identifier, title, collection, section path, page when applicable, tags, and provenance fields.
4. Make retries, pagination, rate limits, timeouts, and incremental change detection explicit. Do not log full user or source content by default.
5. Add unit tests for normal parsing, empty/malformed input, metadata preservation, and failure handling. Use recorded or synthetic fixtures that are safe to redistribute.
6. Wire the connector through the existing service/provider boundary and configuration only where needed. Keep secrets in environment configuration; never hard-code tokens.
7. Run tests and retrieval evaluation, document any connector-specific setup, and include a sample configuration without real credentials in the pull request.

## Pull request checklist

- [ ] The change is scoped and its behavior is described in the PR.
- [ ] Tests cover the new behavior and relevant failure paths.
- [ ] `pytest`, Ruff, Black check, mypy, and/or frontend build pass for touched areas.
- [ ] Retrieval-affecting changes include benchmark results and citation review.
- [ ] Database changes include an Alembic migration and migration validation.
- [ ] API/schema or environment changes are reflected in documentation and `.env.example` where appropriate.
- [ ] Sources and fixtures have clear licence/permission status; no secrets or private data are committed.
- [ ] Logs and error responses avoid leaking secrets or unnecessary document/user content.
- [ ] Operational impacts, rollbacks, and index rebuild needs are noted.