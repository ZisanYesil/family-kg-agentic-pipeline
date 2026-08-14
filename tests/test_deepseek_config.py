from __future__ import annotations

from core import deepseek


def test_deepseek_completion_options(monkeypatch) -> None:
    monkeypatch.setenv("DEEPSEEK_MAX_TOKENS", "4096")

    assert deepseek.completion_options() == {
        "response_format": {"type": "json_object"},
        "max_tokens": 4096,
        "extra_body": {"thinking": {"type": "disabled"}},
    }


def test_deepseek_client_uses_configured_credentials(monkeypatch) -> None:
    captured = {}

    def fake_openai(**kwargs):
        captured.update(kwargs)
        return object()

    monkeypatch.setenv("DEEPSEEK_API_KEY", "test-key")
    monkeypatch.delenv("DEEPSEEK_BASE_URL", raising=False)
    monkeypatch.setattr(deepseek.openai, "OpenAI", fake_openai)

    deepseek.create_client()

    assert captured == {
        "api_key": "test-key",
        "base_url": "https://api.deepseek.com",
    }
