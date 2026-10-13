from abc import ABC, abstractmethod

from app.schemas.knowledge import KnowledgeChunk, KnowledgeFilter, SearchResult


class BaseVectorStore(ABC):
    """Abstract interface for Vector Store implementations."""

    @abstractmethod
    async def initialize(self) -> None:
        """Create or configure collections, vector configurations, and indexes."""

    @abstractmethod
    async def upsert_chunks(self, chunks: list[KnowledgeChunk]) -> int:
        """Upsert chunks with dense and sparse vectors and payload metadata."""

    @abstractmethod
    async def search(
        self,
        dense_vector: list[float] | None,
        sparse_indices: list[int] | None,
        sparse_values: list[float] | None,
        limit: int = 10,
        filter: KnowledgeFilter | None = None,
    ) -> list[SearchResult]:
        """Execute hybrid or dense search with filters."""

    @abstractmethod
    async def delete_by_source(self, source_id: str) -> int:
        """Delete all chunks belonging to a specific source ID."""

    @abstractmethod
    async def count(self) -> int:
        """Count total chunks currently indexed in vector store."""
