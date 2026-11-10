"""Abstract base class for LLM generation adapters."""

from abc import ABC, abstractmethod


class BaseLLMAdapter(ABC):
    """Abstract interface for LLM providers (DeepSeek-R1-Distill-Qwen-32B)."""


    @abstractmethod
    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        temperature: float = 0.2,
    ) -> str:
        """Generate text completion from LLM."""
        ...

    @abstractmethod
    async def is_available(self) -> bool:
        """Check if provider endpoint is accessible and model is loaded."""
        ...
