import logging
import re

from app.core.config import settings
from app.schemas.knowledge import SearchResult
from app.services.knowledge.interfaces.reranker import BaseReranker

logger = logging.getLogger(__name__)


class ConfigurableReranker(BaseReranker):
    """
    Configurable reranker that combines cross-encoder re-scoring (if enabled)
    with query-title-section alignment boosting.
    """

    def __init__(
        self,
        enabled: bool = settings.RERANKER_ENABLED,
        model_name: str = settings.RERANKER_MODEL,
    ):
        self.enabled = enabled
        self.model_name = model_name
        self._cross_encoder = None
        self._initialized = False

    def _init_cross_encoder(self) -> None:
        if self._initialized:
            return
        if self.enabled:
            try:
                # FastEmbed text reranker if available
                from fastembed import TextCrossEncoder  # type: ignore[attr-defined]

                logger.info("Initializing Cross-Encoder model (%s)...", self.model_name)
                self._cross_encoder = TextCrossEncoder(model_name=self.model_name)
            except Exception as e:
                logger.debug(
                    "Cross-encoder not loaded (%s), using lexical alignment reranking",
                    e,
                )
                self._cross_encoder = None
        self._initialized = True

    async def rerank(
        self, query: str, candidates: list[SearchResult], top_k: int
    ) -> list[SearchResult]:
        if not candidates:
            return []

        if not self.enabled:
            return candidates[:top_k]

        self._init_cross_encoder()

        # Try cross-encoder first
        if self._cross_encoder is not None:
            try:
                doc_texts = [
                    f"{c.title} - {c.section_path}: {c.text}" for c in candidates
                ]
                scores = list(self._cross_encoder.rerank(query, doc_texts))
                for c, s in zip(candidates, scores, strict=False):
                    c.score = float(s)
                candidates.sort(key=lambda x: x.score, reverse=True)
                return candidates[:top_k]
            except Exception as e:
                logger.debug(
                    "Cross encoder execution failed (%s), fallback to alignment", e
                )

        # Lexical + hierarchy alignment boosting
        query_terms = [
            t.lower() for t in re.findall(r"\b[a-zA-Z0-9_\-\.]+\b", query) if len(t) > 2
        ]
        if not query_terms:
            return candidates[:top_k]

        for candidate in candidates:
            title_lower = candidate.title.lower()
            section_lower = candidate.section_path.lower()
            text_lower = candidate.text.lower()

            boost = 0.0
            for term in query_terms:
                if term in title_lower:
                    boost += 0.35
                if term in section_lower:
                    boost += 0.25
                if term in text_lower:
                    boost += 0.10

            # Blend existing RRF score with alignment boost
            candidate.score = round(candidate.score * 0.5 + boost * 0.5, 4)

        candidates.sort(key=lambda x: x.score, reverse=True)
        return candidates[:top_k]
