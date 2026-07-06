from __future__ import annotations

import httpx

from tasks.pipeline_task import (
    DEFAULT_MAX_ITERATIONS,
    DEFAULT_WEBHOOK_MAX_ATTEMPTS,
    _max_iterations,
    _trigger_webhook,
)


class _SuccessfulResponse:
    def raise_for_status(self) -> None:
        return None


def test_max_iterations_defaults_when_env_missing() -> None:
    assert _max_iterations({}) == DEFAULT_MAX_ITERATIONS


def test_max_iterations_reads_positive_integer_from_env() -> None:
    assert _max_iterations({"MAX_ITERATIONS": "3"}) == 3


def test_max_iterations_defaults_for_invalid_env_value() -> None:
    assert _max_iterations({"MAX_ITERATIONS": "many"}) == DEFAULT_MAX_ITERATIONS


def test_max_iterations_defaults_for_non_positive_env_value() -> None:
    assert _max_iterations({"MAX_ITERATIONS": "0"}) == DEFAULT_MAX_ITERATIONS


def test_trigger_webhook_retries_http_errors_and_marks_delivered(monkeypatch) -> None:
    attempts: list[str] = []
    delivered_job_ids: list[str] = []

    def fake_post(url: str, **_kwargs):
        attempts.append(url)
        if len(attempts) < DEFAULT_WEBHOOK_MAX_ATTEMPTS:
            raise httpx.ConnectError("connection failed")
        return _SuccessfulResponse()

    monkeypatch.delenv("WEBHOOK_MAX_ATTEMPTS", raising=False)
    monkeypatch.setattr("tasks.pipeline_task.httpx.post", fake_post)
    monkeypatch.setattr(
        "tasks.pipeline_task.database.set_webhook_delivered",
        lambda job_id: delivered_job_ids.append(job_id),
    )

    _trigger_webhook(
        {
            "job_id": "job-1",
            "status": "complete",
            "passed_validation": True,
            "current_iteration": 1,
            "last_error": None,
            "webhook_url": "https://example.com/webhook",
        }
    )

    assert len(attempts) == DEFAULT_WEBHOOK_MAX_ATTEMPTS
    assert delivered_job_ids == ["job-1"]


def test_trigger_webhook_does_not_mark_delivered_when_all_attempts_fail(monkeypatch) -> None:
    attempts: list[str] = []
    delivered_job_ids: list[str] = []

    def fake_post(url: str, **_kwargs):
        attempts.append(url)
        raise httpx.TimeoutException("timed out")

    monkeypatch.setenv("WEBHOOK_MAX_ATTEMPTS", "2")
    monkeypatch.setattr("tasks.pipeline_task.httpx.post", fake_post)
    monkeypatch.setattr(
        "tasks.pipeline_task.database.set_webhook_delivered",
        lambda job_id: delivered_job_ids.append(job_id),
    )

    _trigger_webhook(
        {
            "job_id": "job-1",
            "status": "complete",
            "passed_validation": True,
            "current_iteration": 1,
            "last_error": None,
            "webhook_url": "https://example.com/webhook",
        }
    )

    assert len(attempts) == 2
    assert delivered_job_ids == []


def test_trigger_webhook_does_not_repost_when_mark_delivered_fails(monkeypatch) -> None:
    attempts: list[str] = []

    def fake_post(url: str, **_kwargs):
        attempts.append(url)
        return _SuccessfulResponse()

    def fail_mark_delivered(_job_id: str) -> None:
        raise RuntimeError("database unavailable")

    monkeypatch.setenv("WEBHOOK_MAX_ATTEMPTS", "3")
    monkeypatch.setattr("tasks.pipeline_task.httpx.post", fake_post)
    monkeypatch.setattr(
        "tasks.pipeline_task.database.set_webhook_delivered",
        fail_mark_delivered,
    )

    _trigger_webhook(
        {
            "job_id": "job-1",
            "status": "complete",
            "passed_validation": True,
            "current_iteration": 1,
            "last_error": None,
            "webhook_url": "https://example.com/webhook",
        }
    )

    assert attempts == ["https://example.com/webhook"]
