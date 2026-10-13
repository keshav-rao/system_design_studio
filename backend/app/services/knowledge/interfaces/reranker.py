from abc import ABC, abstractmethod

from app.schemas.knowledge import SearchResult


class BaseReranker(ABC):
    """Abstract interface for Reranker implementations."""

    @abstractmethod
    async def rerank(
        self, query: str, candidates: list[SearchResult], top_k: int
    ) -> list[SearchResult]:
        """
        Rerank a list of candidate SearchResults given the query string.
        Returns top_k re-scored and sorted results.
        """
