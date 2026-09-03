"""Provider-aware configuration for OpenAI-compatible chat completion APIs."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import openai


@dataclass(frozen=True)
class LLMSettings:
    provider: str
    api_key: str | None
    base_url: str | None
    model: str
    timeout_seconds: float
    max_output_tokens: int
    thinking: str


def load_llm_settings() -> LLMSettings:
    base_url = os.getenv("OPENAI_BASE_URL") or None
    provider = os.getenv("LLM_PROVIDER", "").strip().lower()
    if not provider:
        provider = "deepseek" if base_url and "deepseek.com" in base_url.lower() else "openai_compatible"
    model_default = "deepseek-v4-flash" if provider == "deepseek" else "gpt-oss:120b"
    settings = LLMSettings(
        provider=provider,
        api_key=os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY"),
        base_url=base_url,
        model=os.getenv("OPENAI_MODEL", model_default),
        timeout_seconds=float(os.getenv("OPENAI_TIMEOUT_SECONDS", "120")),
        max_output_tokens=int(os.getenv("OPENAI_MAX_COMPLETION_TOKENS", "8000")),
        thinking=os.getenv("DEEPSEEK_THINKING", "disabled").strip().lower(),
    )
    if settings.timeout_seconds <= 0 or settings.max_output_tokens <= 0:
        raise ValueError("LLM timeout and output-token limits must be positive")
    if settings.provider == "deepseek" and settings.thinking not in {"enabled", "disabled"}:
        raise ValueError("DEEPSEEK_THINKING must be enabled or disabled")
    return settings

def create_client(settings: LLMSettings) -> openai.OpenAI:
    client_options: dict[str, Any] = {
        "api_key": settings.api_key,
        "timeout": settings.timeout_seconds,
    }
    if settings.base_url:
        client_options["base_url"] = settings.base_url
    return openai.OpenAI(**client_options)


def completion_parameters(settings: LLMSettings, json_schema_format: dict[str, Any]) -> dict[str, Any]:
    if settings.provider == "deepseek":
        return {
            "response_format": {"type": "json_object"},
            "max_tokens": settings.max_output_tokens,
            "extra_body": {"thinking": {"type": settings.thinking}},
        }
    return {
        "response_format": json_schema_format,
        "max_completion_tokens": settings.max_output_tokens,
    }
