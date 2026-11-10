"""vLLM / OpenAI-compatible adapter for DeepSeek-R1-Distill-Qwen-32B."""

import logging

import httpx

from app.core.config import settings
from app.services.planner.providers.base import BaseLLMAdapter
from app.services.planner.providers.ollama_adapter import clean_deepseek_r1_output

logger = logging.getLogger(__name__)



class VLLMAdapter(BaseLLMAdapter):
    """Adapter connecting to a vLLM server serving DeepSeek-R1-Distill-Qwen-32B."""

    def __init__(
        self,
        base_url: str | None = None,
        model_name: str | None = None,
        api_key: str | None = None,
        timeout: float = 120.0,
    ) -> None:
        self.base_url = (base_url or settings.LLM_BASE_URL).rstrip("/")
        self.model_name = model_name or settings.LLM_MODEL
        self.api_key = api_key or settings.LLM_API_KEY
        self.timeout = timeout

    async def is_available(self) -> bool:
        """Check if vLLM server is responding."""
        try:
            headers = (
                {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
            )
            async with httpx.AsyncClient(timeout=2.0) as client:
                resp = await client.get(f"{self.base_url}/v1/models", headers=headers)
                return resp.status_code == 200
        except Exception:
            return False

    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        temperature: float = 0.2,
    ) -> str:
        """Call vLLM chat completions endpoint."""
        url = f"{self.base_url}/v1/chat/completions"
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        payload = {
            "model": self.model_name,
            "messages": messages,
            "temperature": temperature,
        }

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                resp = await client.post(url, json=payload, headers=headers)
                resp.raise_for_status()
                data = resp.json()
                raw_text = data["choices"][0]["message"]["content"]
                return clean_deepseek_r1_output(raw_text)
        except Exception as e:
            logger.warning(
                "vLLM generation failed (%s). "
                "Falling back to MockLLMAdapter for seamless offline development.",
                e,
            )
            from app.services.planner.providers.mock_adapter import MockLLMAdapter

            return await MockLLMAdapter().generate(prompt, system_prompt, temperature)
