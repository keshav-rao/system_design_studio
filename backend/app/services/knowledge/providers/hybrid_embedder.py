import hashlib
import logging
import math
import re
from collections import Counter

from app.services.knowledge.interfaces.embedder import BaseEmbedder

logger = logging.getLogger(__name__)


def _deterministic_hash(token: str, modulo: int = 10000) -> int:
    """Hash token into a stable integer index for sparse representation."""
    h = int(hashlib.md5(token.encode("utf-8")).hexdigest()[:8], 16)
    return h % modulo


def _tokenize(text: str) -> list[str]:
    """Simple alphanumeric tokenizer."""
    return [w.lower() for w in re.findall(r"\b[a-zA-Z0-9_\-\.]+\b", text) if len(w) > 1]


class HybridEmbedder(BaseEmbedder):
    """
    Hybrid embedder producing dense vectors and sparse token-weight vectors.
    Uses FastEmbed (ONNX) when available, and provides deterministic fallback
    for offline environments and fast unit testing.
    """

    def __init__(
        self,
        dense_model_name: str = "BAAI/bge-small-en-v1.5",
        sparse_model_name: str = "Qdrant/bm25",
        dense_dim: int = 384,
        prefer_fastembed: bool = True,
    ):
        self._dense_model_name = dense_model_name
        self._sparse_model_name = sparse_model_name
        self._dense_dim = dense_dim
        self._prefer_fastembed = prefer_fastembed
        self._dense_model: object | None = None
        self._sparse_model: object | None = None
        self._initialized = False

    @property
    def dense_dimension(self) -> int:
        return self._dense_dim

    def _init_models(self) -> None:
        if self._initialized:
            return
        if self._prefer_fastembed:
            try:
                from fastembed import SparseTextEmbedding, TextEmbedding

                logger.info(
                    "Initializing FastEmbed dense model (%s)...", self._dense_model_name
                )
                self._dense_model = TextEmbedding(model_name=self._dense_model_name)
                logger.info(
                    "Initializing FastEmbed sparse model (%s)...",
                    self._sparse_model_name,
                )
                self._sparse_model = SparseTextEmbedding(
                    model_name=self._sparse_model_name
                )
                logger.info("FastEmbed hybrid models successfully initialized.")
            except Exception as e:
                logger.warning(
                    "FastEmbed initialization failed (%s). "
                    "Falling back to deterministic hybrid embedder.",
                    e,
                )
                self._dense_model = None
                self._sparse_model = None
        self._initialized = True

    def _fallback_dense(self, text: str) -> list[float]:
        """Generate a stable normalized dense representation via term hashing."""
        tokens = _tokenize(text)
        vec = [0.0] * self._dense_dim
        if not tokens:
            return vec

        for i, token in enumerate(tokens):
            h = int(hashlib.sha256(token.encode("utf-8")).hexdigest()[:8], 16)
            idx = h % self._dense_dim
            sign = 1.0 if (h // self._dense_dim) % 2 == 0 else -1.0
            weight = 1.0 / math.sqrt(i + 1)
            vec[idx] += sign * weight

        # L2 normalize
        norm = math.sqrt(sum(x * x for x in vec)) or 1.0
        return [round(x / norm, 6) for x in vec]

    def _fallback_sparse(self, text: str) -> tuple[list[int], list[float]]:
        """Generate BM25-like term frequency sparse vector."""
        tokens = _tokenize(text)
        if not tokens:
            return [], []

        counts = Counter(tokens)
        total = len(tokens)
        pairs: dict[int, float] = {}

        for token, count in counts.items():
            idx = _deterministic_hash(token)
            # TF-like weight with saturation
            tf = count / total
            weight = math.log1p(count) * (1.0 + 0.5 * tf)
            pairs[idx] = round(weight, 4)

        sorted_indices = sorted(pairs.keys())
        sorted_values = [pairs[i] for i in sorted_indices]
        return sorted_indices, sorted_values

    async def embed_query(
        self, text: str
    ) -> tuple[list[float], list[int], list[float]]:
        self._init_models()
        if self._dense_model is not None and self._sparse_model is not None:
            try:
                # FastEmbed returns generators
                dense_gen = self._dense_model.embed([text])  # type: ignore[attr-defined]
                sparse_gen = self._sparse_model.embed([text])  # type: ignore[attr-defined]
                dense = list(next(dense_gen))
                sparse_res = next(sparse_gen)
                return dense, list(sparse_res.indices), list(sparse_res.values)
            except Exception as e:
                logger.warning(
                    "FastEmbed query embedding failed (%s), using fallback.", e
                )

        dense = self._fallback_dense(text)
        s_idx, s_val = self._fallback_sparse(text)
        return dense, s_idx, s_val

    async def embed_documents(
        self, texts: list[str]
    ) -> tuple[list[list[float]], list[list[int]], list[list[float]]]:
        self._init_models()
        if self._dense_model is not None and self._sparse_model is not None:
            try:
                dense_gen = self._dense_model.embed(texts)  # type: ignore[attr-defined]
                sparse_gen = self._sparse_model.embed(texts)  # type: ignore[attr-defined]
                dense_list = [list(d) for d in dense_gen]
                sparse_idx_list: list[list[int]] = []
                sparse_val_list: list[list[float]] = []
                for s in sparse_gen:
                    sparse_idx_list.append(list(s.indices))
                    sparse_val_list.append(list(s.values))
                return dense_list, sparse_idx_list, sparse_val_list
            except Exception as e:
                logger.warning(
                    "FastEmbed doc batch embedding failed (%s), using fallback.", e
                )

        dense_list = [self._fallback_dense(t) for t in texts]
        sparse_idx_list = []
        sparse_val_list = []
        for t in texts:
            idx, val = self._fallback_sparse(t)
            sparse_idx_list.append(idx)
            sparse_val_list.append(val)
        return dense_list, sparse_idx_list, sparse_val_list
