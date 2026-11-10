import logging
import re
from typing import Any

from llama_index.core.schema import NodeWithScore, QueryBundle, TextNode

from app.core.config import settings
from app.schemas.knowledge import SearchResult
from app.services.knowledge.interfaces.reranker import BaseReranker

logger = logging.getLogger(__name__)


class ConfigurableReranker(BaseReranker):
    """
    Reranks hybrid-retrieval candidates.
    provider="cross-encoder" uses LlamaIndex's SentenceTransformerRerank with
    the configured model (BAAI/bge-reranker-v2-m3); load failures raise.
    provider="lexical" uses query/title/section alignment (offline and tests).
    """

    def __init__(
        self,
        enabled: bool = settings.RERANKER_ENABLED,
        model_name: str = settings.RERANKER_MODEL,
        provider: str = "lexical",
        postprocessor: Any | None = None,
    ):
        self.enabled = enabled
        self.model_name = model_name
        self.provider = provider
        self._postprocessor = postprocessor

    def _cross_encoder(self, top_n: int) -> Any:
        if self._postprocessor is None:
            from llama_index.core.postprocessor import SentenceTransformerRerank

            logger.info("Loading cross-encoder reranker (%s)", self.model_name)
            self._postprocessor = SentenceTransformerRerank(
                model=self.model_name, top_n=top_n
            )
        self._postprocessor.top_n = top_n
        return self._postprocessor

    async def rerank(
        self, query: str, candidates: list[SearchResult], top_k: int
    ) -> list[SearchResult]:
        if not candidates:
            return []
        if not self.enabled:
            return candidates[:top_k]
        if self.provider == "cross-encoder":
            return self._rerank_cross_encoder(query, candidates, top_k)
        return self._rerank_lexical(query, candidates, top_k)

    def _rerank_cross_encoder(
        self, query: str, candidates: list[SearchResult], top_k: int
    ) -> list[SearchResult]:
        by_id = {c.chunk_id: c for c in candidates}
        nodes = [
            NodeWithScore(
                node=TextNode(
                    id_=c.chunk_id, text=f"{c.title} - {c.section_path}: {c.text}"
                ),
                score=c.score,
            )
            for c in candidates
        ]
        ranked = self._cross_encoder(top_k).postprocess_nodes(
            nodes, query_bundle=QueryBundle(query)
        )
        results: list[SearchResult] = []
        for n in ranked:
            result = by_id[n.node.node_id].model_copy()
            result.score = float(n.score or 0.0)
            results.append(result)
        return results

    @staticmethod
    def _rerank_lexical(
        query: str, candidates: list[SearchResult], top_k: int
    ) -> list[SearchResult]:
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

            candidate.score = round(candidate.score * 0.5 + boost * 0.5, 4)

        candidates.sort(key=lambda x: x.score, reverse=True)
        return candidates[:top_k]
