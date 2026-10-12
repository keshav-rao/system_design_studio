# Tech Context

## Technology Stack

### Backend
- **Language**: Python 3.11+ (running 3.13)
- **Framework**: FastAPI with Pydantic v2 & `pydantic-settings`
- **Database**: PostgreSQL 16 with async SQLAlchemy and Alembic migrations
- **Vector DB**: Qdrant (dense + sparse vectors)
- **Embedding & Reranking**: BAAI/bge-m3, BAAI/bge-reranker-v2-m3
- **LLM Adapter**: DeepSeek-R1-Distill-Qwen-32B via vLLM / Ollama

### Frontend
- **Framework**: React 18 / 19, TypeScript
- **Tooling**: Vite
- **Canvas Engine**: React Flow (`@xyflow/react`)
- **Styling**: Tailwind CSS & Modern Web Design Tokens
- **State Management**: TanStack Query (server state), Zustand (canvas/interaction state)

### Infrastructure
- Docker Compose for PostgreSQL, Qdrant, and Backend services.
