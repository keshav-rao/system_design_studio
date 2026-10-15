"""Ollama adapter for DeepSeek-R1-Distill-Qwen-32B."""

import logging
import re

import httpx

from app.core.config import settings
from app.services.planner.providers.base import BaseLLMAdapter

logger = logging.getLogger(__name__)


def clean_deepseek_r1_output(raw_text: str) -> str:
    """Remove chain-of-thought <think>...</think> tags if present."""
    # Strip <think>...</think> block
    cleaned = re.sub(r"<think>.*?</think>", "", raw_text, flags=re.DOTALL).strip()
    # Strip markdown code blocks ```json ... ``` if model wrapped it
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
    return cleaned.strip()


class OllamaAdapter(BaseLLMAdapter):
    """Adapter connecting to Ollama running DeepSeek-R1-Distill-Qwen-32B."""

    def __init__(
        self,
        base_url: str | None = None,
        model_name: str | None = None,
        timeout: float = 120.0,
    ) -> None:
        self.base_url = (base_url or settings.LLM_BASE_URL).rstrip("/")
        self.model_name = model_name or settings.LLM_MODEL
        self.timeout = timeout

    async def is_available(self) -> bool:
        """Check if Ollama service is reachable."""
        try:
            async with httpx.AsyncClient(timeout=2.0) as client:
                resp = await client.get(f"{self.base_url}/api/tags")
                return resp.status_code == 200
        except Exception:
            return False

    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        temperature: float = 0.2,
    ) -> str:
        """Query Ollama generate API."""
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "system": system_prompt or "",
            "stream": False,
            "options": {
                "temperature": temperature,
            },
        }

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                resp = await client.post(url, json=payload)
                resp.raise_for_status()
                data = resp.json()
                raw_response = data.get("response", "")
                return clean_deepseek_r1_output(raw_response)
        except Exception as e:
            logger.warning(
                "Ollama generation failed for model %s (%s). "
                "Falling back to MockLLMAdapter for seamless offline development.",
                self.model_name,
                e,
            )
            from app.services.planner.providers.mock_adapter import MockLLMAdapter

            return await MockLLMAdapter().generate(prompt, system_prompt, temperature)
