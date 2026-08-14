from __future__ import annotations

import os
from typing import Any

import openai

DEEPSEEK_MODEL = "deepseek-v4-flash"
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEFAULT_MAX_TOKENS = 8192
JSON_RESPONSE_FORMAT = {"type": "json_object"}
THINKING_DISABLED = {"thinking": {"type": "disabled"}}


def get_model() -> str:
    return os.getenv("DEEPSEEK_MODEL", DEEPSEEK_MODEL)


def get_max_tokens() -> int:
    raw_value = os.getenv("DEEPSEEK_MAX_TOKENS", str(DEFAULT_MAX_TOKENS))
    try:
        value = int(raw_value)
    except ValueError as exc:
        raise ValueError("DEEPSEEK_MAX_TOKENS must be an integer") from exc
    if value <= 0:
        raise ValueError("DEEPSEEK_MAX_TOKENS must be greater than zero")
    return value


def create_client() -> openai.OpenAI:
    return openai.OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url=os.getenv("DEEPSEEK_BASE_URL", DEEPSEEK_BASE_URL),
    )


def completion_options() -> dict[str, Any]:
    """Options required by DeepSeek JSON mode with reasoning disabled."""
    return {
        "response_format": JSON_RESPONSE_FORMAT.copy(),
        "max_tokens": get_max_tokens(),
        "extra_body": {"thinking": THINKING_DISABLED["thinking"].copy()},
    }
