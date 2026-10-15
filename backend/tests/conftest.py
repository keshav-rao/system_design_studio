from collections.abc import AsyncGenerator

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.database import Base, get_db
from app.main import app
from app.models.catalog import Component, ComponentCompatibility  # noqa: F401
from app.models.project import DesignVersion, Project  # noqa: F401
from app.models.source import EvalQuestion, EvalRun, Source  # noqa: F401
from app.services.knowledge.providers.hybrid_embedder import HybridEmbedder
from app.services.knowledge.providers.qdrant_store import QdrantVectorStore
from app.services.knowledge.providers.reranker import ConfigurableReranker
from app.services.knowledge.service import KnowledgeService, get_knowledge_service

# Test SQLite async engine
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestSessionLocal = async_sessionmaker(
    bind=test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@pytest_asyncio.fixture(scope="function")
async def test_db() -> AsyncGenerator[AsyncSession, None]:
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with TestSessionLocal() as session:
        yield session

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
def test_knowledge_service() -> KnowledgeService:
    # Use in-memory Qdrant and fast deterministic embedder
    store = QdrantVectorStore(collection_name="test_chunks", force_memory=True)
    embedder = HybridEmbedder(prefer_fastembed=False)  # fast deterministic embedder
    reranker = ConfigurableReranker(enabled=True)
    return KnowledgeService(
        vector_store=store,
        embedder=embedder,
        reranker=reranker,
    )


@pytest_asyncio.fixture(scope="function")
async def async_client(
    test_db: AsyncSession, test_knowledge_service: KnowledgeService
) -> AsyncGenerator[AsyncClient, None]:
    async def override_get_db() -> AsyncGenerator[AsyncSession, None]:
        yield test_db

    def override_get_knowledge_service() -> KnowledgeService:
        return test_knowledge_service

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_knowledge_service] = override_get_knowledge_service

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client

    app.dependency_overrides.clear()
