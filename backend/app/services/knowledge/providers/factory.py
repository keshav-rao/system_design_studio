from app.core.config import settings
from app.services.knowledge.interfaces.embedder import BaseEmbedder
from app.services.knowledge.providers.bge_m3_embedder import BGEM3Embedder
from app.services.knowledge.providers.hybrid_embedder import HybridEmbedder
from app.services.knowledge.providers.reranker import ConfigurableReranker


def build_embedder(provider: str | None = None) -> BaseEmbedder:
    provider = (provider or settings.EMBEDDING_PROVIDER).lower()
    if provider == "bge-m3":
        return BGEM3Embedder(
            model_name=settings.EMBEDDING_MODEL,
            device=settings.EMBEDDING_DEVICE,
            batch_size=settings.EMBEDDING_BATCH_SIZE,
            max_length=settings.EMBEDDING_MAX_LENGTH,
        )
    if provider == "fastembed":
        return HybridEmbedder(
            dense_model_name=settings.EMBEDDING_MODEL,
            sparse_model_name=settings.SPARSE_EMBEDDING_MODEL,
            prefer_fastembed=True,
            strict=True,
        )
    if provider == "hash":
        return HybridEmbedder(prefer_fastembed=False)
    raise ValueError(f"Unknown EMBEDDING_PROVIDER: {provider!r}")


def build_reranker() -> ConfigurableReranker:
    return ConfigurableReranker(
        enabled=settings.RERANKER_ENABLED,
        model_name=settings.RERANKER_MODEL,
        provider=settings.RERANKER_PROVIDER,
    )
