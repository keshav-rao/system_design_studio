from abc import ABC, abstractmethod


class BaseEmbedder(ABC):
    """Abstract interface for hybrid dense and sparse embeddings."""

    @property
    @abstractmethod
    def dense_dimension(self) -> int:
        """Returns the dimension size of the dense vector."""

    @abstractmethod
    async def embed_query(
        self, text: str
    ) -> tuple[list[float], list[int], list[float]]:
        """
        Embed a single search query text.
        Returns: (dense_vector, sparse_indices, sparse_values)
        """

    @abstractmethod
    async def embed_documents(
        self, texts: list[str]
    ) -> tuple[list[list[float]], list[list[int]], list[list[float]]]:
        """
        Embed a batch of document chunk texts.
        Returns: (dense_vectors, sparse_indices_batch, sparse_values_batch)
        """
