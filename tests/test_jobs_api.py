from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import pytest
from fastapi import HTTPException, status

from api.models.job import GraphFormat, JobCreateRequest, JobStatus
from api.routers.jobs import (
    create_kg_extraction_job,
    get_iteration_history,
    get_kg_extraction_status,
    get_validated_graph,
)


class _FakeStorage:
    def __init__(
        self,
        job: dict[str, Any] | None = None,
        iterations: list[dict[str, Any]] | None = None,
        read_after_create: bool = True,
    ) -> None:
        self._job = job
        self._iterations = iterations or []
        self._read_after_create = read_after_create
        self.created_jobs: list[dict[str, Any]] = []

    def create_job(
        self,
        job_id: str,
        input_text: str,
        ontology_path: str,
        max_iterations: int,
        webhook_url: str | None,
    ) -> None:
        self.created_jobs.append(
            {
                "job_id": job_id,
                "input_text": input_text,
                "ontology_path": ontology_path,
                "max_iterations": max_iterations,
                "webhook_url": webhook_url,
            }
        )
        if self._read_after_create:
            self._job = _job(JobStatus.Pending, job_id=job_id)

    def get_job(self, _job_id: str) -> dict[str, Any] | None:
        return self._job

    def get_iterations(self, _job_id: str) -> list[dict[str, Any]]:
        return self._iterations


def _job(
    status_value: JobStatus,
    graph_turtle: str | None = None,
    job_id: str = "job-1",
    passed_validation: bool = False,
) -> dict[str, Any]:
    now = datetime.now(timezone.utc)
    return {
        "job_id": job_id,
        "status": status_value.value,
        "input_text": "Jane Doe was born in 1900.",
        "current_iteration": 2,
        "max_iterations": 10,
        "last_error": None,
        "graph_turtle": graph_turtle,
        "passed_validation": passed_validation,
        "webhook_url": None,
        "webhook_delivered": False,
        "created_at": now,
        "updated_at": now,
    }


def _iteration(iteration_number: int = 1) -> dict[str, Any]:
    return {
        "iteration_number": iteration_number,
        "violations": ["Missing rdf:type for fhkb:jane"],
        "llm_reasoning": "Added the missing Person type.",
        "triples_before": 3,
        "triples_after": 4,
        "timestamp": datetime.now(timezone.utc),
    }


def test_create_kg_extraction_job_persists_and_dispatches(monkeypatch) -> None:
    dispatched_job_ids: list[str] = []
    storage = _FakeStorage()

    monkeypatch.setenv("MAX_ITERATIONS", "7")
    monkeypatch.setenv("DEFAULT_ONTOLOGY_PATH", "ontology/family_extended.ttl")
    monkeypatch.setattr(
        "api.routers.jobs.dispatch_extraction_job",
        lambda job_id: dispatched_job_ids.append(job_id),
    )

    response = create_kg_extraction_job(
        JobCreateRequest(text="Jane Doe was born in 1900 and married John Doe."),
        db=storage,
    )

    assert response.status == JobStatus.Pending
    assert storage.created_jobs == [
        {
            "job_id": response.job_id,
            "input_text": "Jane Doe was born in 1900 and married John Doe.",
            "ontology_path": "ontology/family_extended.ttl",
            "max_iterations": 7,
            "webhook_url": None,
        }
    ]
    assert dispatched_job_ids == [response.job_id]


def test_create_kg_extraction_job_uses_request_ontology_path_when_given(
    monkeypatch,
) -> None:
    storage = _FakeStorage()
    monkeypatch.delenv("DEFAULT_ONTOLOGY_PATH", raising=False)
    monkeypatch.setattr("api.routers.jobs.dispatch_extraction_job", lambda _job_id: None)

    create_kg_extraction_job(
        JobCreateRequest(
            text="Jane Doe was born in 1900 and married John Doe.",
            ontology_path="ontology/custom.ttl",
        ),
        db=storage,
    )

    assert storage.created_jobs[0]["ontology_path"] == "ontology/custom.ttl"


def test_create_kg_extraction_job_422s_when_no_ontology_path_available(
    monkeypatch,
) -> None:
    storage = _FakeStorage()
    monkeypatch.delenv("DEFAULT_ONTOLOGY_PATH", raising=False)
    monkeypatch.setattr("api.routers.jobs.dispatch_extraction_job", lambda _job_id: None)

    with pytest.raises(HTTPException) as exc_info:
        create_kg_extraction_job(
            JobCreateRequest(text="Jane Doe was born in 1900 and married John Doe."),
            db=storage,
        )

    assert exc_info.value.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert storage.created_jobs == []


def test_create_kg_extraction_job_errors_when_created_job_cannot_be_read(
    monkeypatch,
) -> None:
    storage = _FakeStorage(read_after_create=False)
    monkeypatch.setenv("DEFAULT_ONTOLOGY_PATH", "ontology/family_extended.ttl")
    monkeypatch.setattr("api.routers.jobs.dispatch_extraction_job", lambda _job_id: None)

    with pytest.raises(HTTPException) as exc_info:
        create_kg_extraction_job(
            JobCreateRequest(text="Jane Doe was born in 1900 and married John Doe."),
            db=storage,
        )

    assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


def test_get_kg_extraction_status_returns_job_state() -> None:
    response = get_kg_extraction_status(
        "job-1",
        db=_FakeStorage(_job(JobStatus.Validating)),
    )

    assert response.job_id == "job-1"
    assert response.status == JobStatus.Validating
    assert response.current_iteration == 2
    assert response.max_iterations == 10


def test_get_kg_extraction_status_returns_404_for_missing_job() -> None:
    with pytest.raises(HTTPException) as exc_info:
        get_kg_extraction_status("missing-job", db=_FakeStorage(None))

    assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.parametrize(
    "job_status",
    [
        JobStatus.Pending,
        JobStatus.Extracting,
        JobStatus.Building,
        JobStatus.Validating,
        JobStatus.Repairing,
        JobStatus.Error,
        JobStatus.MaxIterationsReached,
    ],
)
def test_get_validated_graph_rejects_incomplete_jobs(job_status: JobStatus) -> None:
    with pytest.raises(HTTPException) as exc_info:
        get_validated_graph("job-1", db=_FakeStorage(_job(job_status)))

    assert exc_info.value.status_code == status.HTTP_409_CONFLICT
    assert job_status.value in exc_info.value.detail


def test_get_validated_graph_allows_complete_empty_graph() -> None:
    response = get_validated_graph(
        "job-1",
        format=GraphFormat.turtle,
        db=_FakeStorage(_job(JobStatus.Complete, graph_turtle="")),
    )

    assert response.job_id == "job-1"
    assert response.triple_count == 0


def test_get_validated_graph_returns_complete_graph() -> None:
    response = get_validated_graph(
        "job-1",
        format=GraphFormat.turtle,
        db=_FakeStorage(
            _job(
                JobStatus.Complete,
                graph_turtle="""
                    @prefix fhkb: <http://example.org/family#> .
                    fhkb:jane a fhkb:Person .
                """,
                passed_validation=True,
            )
        ),
    )

    assert response.job_id == "job-1"
    assert response.format == GraphFormat.turtle
    assert "fhkb:jane" in response.graph_content
    assert response.triple_count == 1
    assert response.passed_validation is True


def test_get_validated_graph_returns_404_for_missing_job() -> None:
    with pytest.raises(HTTPException) as exc_info:
        get_validated_graph("missing-job", db=_FakeStorage(None))

    assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND


def test_get_iteration_history_returns_iterations() -> None:
    response = get_iteration_history(
        "job-1",
        db=_FakeStorage(_job(JobStatus.Repairing), iterations=[_iteration()]),
    )

    assert response.job_id == "job-1"
    assert len(response.iterations) == 1
    assert response.iterations[0].iteration_number == 1
    assert response.iterations[0].violations == ["Missing rdf:type for fhkb:jane"]


def test_get_iteration_history_returns_404_for_missing_job() -> None:
    with pytest.raises(HTTPException) as exc_info:
        get_iteration_history("missing-job", db=_FakeStorage(None))

    assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND