import asyncio
import logging
from typing import Any

from app.services.knowledge.interfaces.embedder import BaseEmbedder

logger = logging.getLogger(__name__)

BGE_M3_DENSE_DIM = 1024


class BGEM3Embedder(BaseEmbedder):
    """
    BAAI/bge-m3 via FlagEmbedding: one forward pass yields the 1024-d dense
    vector and the learned lexical (sparse) weights used for hybrid search.
    Model load failures raise; there is no silent fallback.
    """

    def __init__(
        self,
        model_name: str = "BAAI/bge-m3",
        device: str | None = None,
        batch_size: int = 16,
        max_length: int = 1024,
        model: Any | None = None,
    ):
        self._model_name = model_name
        self._device = device
        self._batch_size = batch_size
        self._max_length = max_length
        self._model = model

    @property
    def dense_dimension(self) -> int:
        return BGE_M3_DENSE_DIM

    def _load(self) -> Any:
        if self._model is None:
            import torch
            from FlagEmbedding import BGEM3FlagModel

            device = self._device or ("cuda" if torch.cuda.is_available() else "cpu")
            logger.info("Loading %s on %s", self._model_name, device)
            self._model = BGEM3FlagModel(
                self._model_name, use_fp16=device.startswith("cuda"), devices=device
            )
        return self._model

    def _encode(
        self, texts: list[str]
    ) -> tuple[list[list[float]], list[list[int]], list[list[float]]]:
        out = self._load().encode(
            texts,
            batch_size=self._batch_size,
            max_length=self._max_length,
            return_dense=True,
            return_sparse=True,
            return_colbert_vecs=False,
        )
        dense = [[float(x) for x in vec] for vec in out["dense_vecs"]]
        indices: list[list[int]] = []
        values: list[list[float]] = []
        for weights in out["lexical_weights"]:
            pairs = sorted((int(k), float(v)) for k, v in weights.items())
            indices.append([k for k, _ in pairs])
            values.append([v for _, v in pairs])
        return dense, indices, values

    async def embed_query(
        self, text: str
    ) -> tuple[list[float], list[int], list[float]]:
        dense, indices, values = await asyncio.to_thread(self._encode, [text])
        return dense[0], indices[0], values[0]

    async def embed_documents(
        self, texts: list[str]
    ) -> tuple[list[list[float]], list[list[int]], list[list[float]]]:
        if not texts:
            return [], [], []
        return await asyncio.to_thread(self._encode, texts)
