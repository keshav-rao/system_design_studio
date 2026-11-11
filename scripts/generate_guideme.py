"""Generate the developer onboarding and architecture guide as guideme.docx.

Install the optional dependency with ``python -m pip install python-docx`` and run
``python scripts/generate_guideme.py`` from the repository root.
"""

from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_BREAK, WD_LINE_SPACING
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "guideme.docx"


def add_code(document: Document, text: str) -> None:
    paragraph = document.add_paragraph(style="No Spacing")
    paragraph.paragraph_format.left_indent = Inches(0.18)
    paragraph.paragraph_format.space_after = Pt(6)
    for index, line in enumerate(text.strip("\n").splitlines()):
        if index:
            paragraph.add_run().add_break(WD_BREAK.LINE)
        run = paragraph.add_run(line)
        run.font.name = "Consolas"
        run.font.size = Pt(8.5)
        run.font.color.rgb = RGBColor(40, 70, 90)


def add_table(document: Document, headers: list[str], rows: list[list[str]]) -> None:
    table = document.add_table(rows=1, cols=len(headers))
    table.style = "Light Shading Accent 1"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for cell, value in zip(table.rows[0].cells, headers):
        cell.text = value
    for row in rows:
        cells = table.add_row().cells
        for cell, value in zip(cells, row):
            cell.text = value


def build_document() -> None:
    document = Document()
    section = document.sections[0]
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

    styles = document.styles
    styles["Normal"].font.name = "Aptos"
    styles["Normal"].font.size = Pt(10)
    styles["Normal"].paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    for name, size, color in [
        ("Title", 28, RGBColor(18, 74, 92)),
        ("Heading 1", 19, RGBColor(18, 74, 92)),
        ("Heading 2", 14, RGBColor(36, 105, 117)),
    ]:
        styles[name].font.name = "Aptos Display"
        styles[name].font.size = Pt(size)
        styles[name].font.color.rgb = color

    document.add_heading("System Design Studio", 0)
    subtitle = document.add_paragraph("Developer Onboarding & Architecture Guide")
    subtitle.style = "Subtitle"
    document.add_paragraph(
        "A practical guide to the repository, local setup, knowledge ingestion, "
        "retrieval, planning, and engineering workflow."
    )

    document.add_heading("1. System Architecture Overview", level=1)
    document.add_paragraph(
        "System Design Studio turns application requirements into evidence-backed "
        "architecture proposals. The React canvas calls a FastAPI API. The knowledge "
        "service retrieves relevant technical sources from Qdrant; the planner combines "
        "those sources with catalog data and user requirements; Pydantic schema checks "
        "and deterministic validation run before results return to the client."
    )
    add_table(
        document,
        ["Stage", "Responsibility", "Technology"],
        [
            ["Ingestion", "Parse permitted PDFs/Markdown; preserve provenance", "Python parsers, LlamaIndex"],
            ["Indexing", "Create dense and sparse vectors and searchable payloads", "BGE-M3, Qdrant"],
            ["Retrieval", "Hybrid candidate search followed by optional reranking", "Qdrant RRF, BGE reranker"],
            ["Planning", "Generate a typed design proposal from requirements and evidence", "LangGraph, configured LLM"],
            ["Validation", "Check deterministic architecture and catalog constraints", "Python rule functions"],
            ["Persistence/UI", "Persist projects and show editable architecture designs", "PostgreSQL, FastAPI, React Flow"],
        ],
    )
    add_code(
        document,
        "Raw source -> parser -> metadata + chunks -> embeddings -> Qdrant\n"
        "User request -> FastAPI -> hybrid retrieval -> reranker -> planner\n"
        "Planner output -> Pydantic schema -> deterministic validator -> React canvas",
    )

    document.add_heading("2. Environment & Setup", level=1)
    document.add_paragraph(
        "Prerequisites: Docker Compose, Python 3.11+, and Node.js/npm. The local "
        "Compose stack provides PostgreSQL 16, Qdrant, the API, and frontend. Ollama "
        "is configured as the default LLM endpoint but is not a Compose service in the "
        "current repository; start it separately if using the local model. The Compose "
        "file forwards only selected variables, so add provider overrides to the "
        "backend.environment mapping. For host-installed Ollama, pass LLM_BASE_URL as "
        "http://host.docker.internal:11434; container localhost is not the host."
    )
    document.add_heading("Initial setup", level=2)
    add_code(
        document,
        "# Repository root\n"
        "Copy-Item .env.example .env  # PowerShell\n"
        "docker compose up -d --build\n"
        "docker compose exec backend alembic upgrade head\n"
        "\n"
        "# Backend-local development (PowerShell)\n"
        "cd backend\n"
        "Copy-Item ..\\.env.example .env\n"
        "python -m venv .venv\n"
        ".venv\\Scripts\\Activate.ps1\n"
        "python -m pip install -r requirements.txt\n"
        "alembic upgrade head\n"
        "uvicorn app.main:app --reload --host 0.0.0.0 --port 8000",
    )
    document.add_paragraph(
        "On macOS/Linux, activate with `source .venv/bin/activate`. When running the "
        "backend locally, ensure PostgreSQL and Qdrant are available first. The API "
        "does not automatically apply Alembic migrations during application startup."
    )
    document.add_heading("Environment variables", level=2)
    add_table(
        document,
        ["Variable", "Purpose / current default"],
        [
            ["APP_NAME, ENVIRONMENT, DEBUG, HOST, PORT", "Application identity, mode, docs visibility, bind address/port"],
            ["DATABASE_URL", "Async SQLAlchemy URL; Compose wires PostgreSQL service credentials"],
            ["POSTGRES_USER/PASSWORD/DB/PORT", "Local PostgreSQL container settings; replace weak credentials outside local development"],
            ["QDRANT_URL, QDRANT_COLLECTION", "Qdrant endpoint and collection name"],
            ["EMBEDDING_PROVIDER/MODEL/DEVICE", "Default bge-m3; `hash` is for lightweight tests/offline development"],
            ["RERANKER_PROVIDER/MODEL/ENABLED", "Default cross-encoder; `lexical` is a lightweight development option"],
            ["RAG_CORPUS_PATH, RAG_CHUNK_SIZE, RAG_CHUNK_OVERLAP", "Corpus path and chunking defaults (512 / 64)"],
            ["LLM_PROVIDER/MODEL/BASE_URL/API_KEY", "Default Ollama endpoint and configured DeepSeek model; API key is optional and must remain secret"],
            ["ALLOWED_ORIGINS, LOG_LEVEL", "CORS allowlist and log verbosity"],
        ],
    )
    document.add_paragraph(
        "Settings are defined in backend/app/core/config.py. The checked-in "
        ".env.example shows basic service settings; all supported defaults are in "
        "the Settings class. Never commit secrets."
    )
    document.add_heading("Local service URLs", level=2)
    add_table(
        document,
        ["Service", "URL"],
        [
            ["Frontend", "http://localhost:3000"],
            ["API / Swagger (DEBUG=true)", "http://localhost:8000/docs"],
            ["Health", "http://localhost:8000/health"],
            ["Qdrant dashboard", "http://localhost:6333/dashboard"],
            ["PostgreSQL", "localhost:5432"],
        ],
    )

    document.add_heading("3. Directory & File Walkthrough", level=1)
    add_table(
        document,
        ["Path", "Responsibility"],
        [
            ["backend/app/api/", "FastAPI transport, versioned routers, request/response wiring"],
            ["backend/app/api/v1/", "Versioned health, knowledge, catalog, validator, and project routes"],
            ["backend/app/cli/", "Command-line maintenance and corpus ingestion entry points"],
            ["backend/app/core/", "Settings, database setup, shared application infrastructure"],
            ["backend/app/data/", "Backend-owned seed/reference data"],
            ["backend/app/models/", "SQLAlchemy ORM entities"],
            ["backend/app/repositories/", "Database persistence access"],
            ["backend/app/schemas/", "Pydantic API and domain contracts"],
            ["backend/app/services/", "Knowledge, planning, catalog, and validation logic"],
            ["backend/app/services/catalog/", "Catalog business logic and component compatibility"],
            ["backend/app/services/knowledge/", "Knowledge ingestion, indexing, search, and evaluation"],
            ["backend/app/services/knowledge/ingestion/", "Source parsers and chunking pipeline"],
            ["backend/app/services/knowledge/interfaces/", "Provider contracts for replaceable RAG components"],
            ["backend/app/services/knowledge/providers/", "Embedding, Qdrant store, and reranker implementations"],
            ["backend/app/services/planner/", "Requirement planning and LLM orchestration"],
            ["backend/app/services/validator/", "Deterministic design validation rules"],
            ["backend/alembic/", "Database migration environment and revisions"],
            ["backend/tests/", "Backend unit and API integration tests"],
            ["frontend/src/", "React application, components, API clients, state, and types"],
            ["frontend/src/api/", "Frontend API client and request integration"],
            ["frontend/src/components/", "Reusable UI and canvas components"],
            ["frontend/src/data/", "Frontend-owned static data and defaults"],
            ["frontend/src/store/", "Client-side application state"],
            ["frontend/src/types/", "TypeScript domain and API-facing types"],
            ["rag_knowledge_base/", "Authoritative technical corpus organized into collections"],
            ["data/", "Evaluation questions and seed knowledge inputs"],
            ["docs/", "Long-form project documentation"],
            ["implementation/", "Product, UX, schema, and implementation planning artifacts"],
            ["MEMORY_BANK/", "Maintained product context, decisions, patterns, and progress"],
            ["scripts/", "Repository maintenance scripts and documentation generators"],
            ["backend/alembic/versions/", "Versioned database migration scripts"],
            ["rag_knowledge_base/<collection>/", "Curated source files grouped for ingestion and retrieval filtering"],
            ["tests/", "Repository-level tests, including backend test suite"],
            ["docker-compose.yml", "Local PostgreSQL, Qdrant, API, and frontend services"],
            ["backend/app/main.py", "FastAPI app, lifecycle, CORS, health, and API router registration"],
            ["backend/app/core/config.py", "Environment-backed application and provider settings"],
            ["backend/app/cli/ingest_corpus.py", "Incremental/full corpus ingestion and optional evaluation"],
            ["backend/pyproject.toml", "Ruff, Black, and mypy configuration"],
            ["backend/requirements.txt", "Python application and test dependencies"],
            ["backend/alembic.ini", "Alembic migration configuration"],
            ["frontend/package.json", "Frontend dependencies and Vite/build scripts"],
            ["frontend/src/App.tsx", "Top-level frontend application and view composition"],
            ["frontend/src/main.tsx", "Browser entry point that mounts the React application"],
            ["frontend/src/index.css", "Global frontend styles and base design rules"],
            ["frontend/vite.config.ts", "Vite dev server, port, and API proxy configuration"],
            ["backend/Dockerfile / frontend/Dockerfile", "Container build/runtime definitions for API and web app"],
            [".env.example", "Sample local environment configuration; contains development values only"],
            ["README.md / ARCHITECTURE.md / CONTRIBUTING.md", "Project entry point, technical design, and contributor workflow"],
        ],
    )

    document.add_heading("4. Data Ingestion & Retrieval Workflow", level=1)
    document.add_paragraph(
        "The repository corpus under rag_knowledge_base/ is authoritative; top-level "
        "folders define collection names. Keep licence/permission and source metadata "
        "with every source. The current CLI supports selecting collections, incremental "
        "updates, full rebuilds, and an evaluation run."
    )
    add_code(
        document,
        "cd backend\n"
        "python -m app.cli.ingest_corpus --recreate --eval  # first build/model change\n"
        "python -m app.cli.ingest_corpus                    # incremental changed files\n"
        "python -m app.cli.ingest_corpus --collections 03_component_decision_guides",
    )
    add_table(
        document,
        ["Step", "What happens"],
        [
            ["Parse", "Format-specific parser extracts text and source location metadata."],
            ["Chunk", "Text is split into approximately 512-token pieces with 64-token overlap; preserve headings/section paths."],
            ["Embed", "BGE-M3 generates dense and sparse vectors; configured providers can be swapped."],
            ["Index", "Qdrant stores vectors and payload metadata for hybrid retrieval."],
            ["Retrieve", "Dense and sparse candidates are fused; filters and score thresholds may be applied."],
            ["Rerank", "Cross-encoder reranker reorders candidates for query relevance; lexical mode supports light development."],
            ["Ground and generate", "Planner consumes selected chunks, catalog facts, and requirements; typed output is validated."],
            ["Evaluate", "Use MRR, recall@3/5, citation correctness, schema validity, and human review after RAG changes."],
        ],
    )
    document.add_paragraph(
        "A full BGE-M3 ingestion and cross-encoder workload is compute intensive; "
        "GPU acceleration is recommended. `EMBEDDING_PROVIDER=hash`, "
        "`RERANKER_PROVIDER=lexical`, and `LLM_PROVIDER=mock` are useful for fast "
        "offline development but do not represent production semantic quality."
    )

    document.add_heading("5. Development & Deployment Standards", level=1)
    document.add_heading("Branches and review", level=2)
    document.add_paragraph(
        "Use short kebab-case branches such as feat/notion-loader or fix/citation-metadata. "
        "Keep pull requests focused and include tests, migration notes, evaluation "
        "results for retrieval-affecting changes, and security/data-rights considerations. "
        "Do not commit credentials, model weights, generated indexes, or unlicensed data."
    )
    document.add_heading("Tests and static checks", level=2)
    add_code(
        document,
        "cd backend\n"
        "pytest\n"
        "ruff check .\n"
        "black --check .\n"
        "mypy app\n"
        "\n"
        "# Frontend type check and production build, from repository root\n"
        "npm --prefix frontend run build",
    )
    document.add_heading("API startup and example", level=2)
    add_code(
        document,
        "docker compose up -d --build\n"
        "docker compose exec backend alembic upgrade head\n"
        "# API docs: http://localhost:8000/docs\n"
        "\n"
        "curl -X POST http://localhost:8000/api/v1/knowledge/search \\\n"
        "  -H 'Content-Type: application/json' \\\n"
        "  -d '{\"query\":\"database failover strategies\",\"limit\":5,\"use_reranker\":true}'",
    )
    document.add_paragraph(
        "Production deployments should use managed secrets, TLS, restricted network "
        "access, authentication/authorization, resource limits, observability, tested "
        "database and vector-index backups, and a documented restore/rebuild procedure. "
        "The Compose configuration is the local development baseline, not a complete "
        "production security configuration."
    )

    document.save(OUTPUT)
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    build_document()