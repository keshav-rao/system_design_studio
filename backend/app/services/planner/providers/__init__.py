"""LLM Provider factory."""

import logging

from app.core.config import settings
from app.services.planner.providers.base import BaseLLMAdapter
from app.services.planner.providers.mock_adapter import MockLLMAdapter
from app.services.planner.providers.ollama_adapter import OllamaAdapter
from app.services.planner.providers.vllm_adapter import VLLMAdapter

logger = logging.getLogger(__name__)


def get_llm_adapter(provider_override: str | None = None) -> BaseLLMAdapter:
    """Return configured LLM adapter based on settings or override."""
    provider = (provider_override or settings.LLM_PROVIDER).lower()

    if provider == "ollama":
        return OllamaAdapter()
    elif provider == "vllm":
        return VLLMAdapter()
    elif provider == "mock":
        return MockLLMAdapter()
    else:
        logger.warning(
            "Unknown LLM_PROVIDER '%s'. Defaulting to MockLLMAdapter.", provider
        )
        return MockLLMAdapter()


__all__ = [
    "BaseLLMAdapter",
    "MockLLMAdapter",
    "OllamaAdapter",
    "VLLMAdapter",
    "get_llm_adapter",
]
