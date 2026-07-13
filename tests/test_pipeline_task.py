from __future__ import annotations

import httpx

from agents.kg_builder_agent import KGBuilderResult
from agents.ontology_mapping_agent import OntologyMappingAgentError, OntologyMappingResult
from api.models.job import JobStatus
from ontology.schema_loader import OntologySchema, OntologySchemaError
from tasks.pipeline_task import (
    DEFAULT_MAX_ITERATIONS,
    DEFAULT_WEBHOOK_MAX_ATTEMPTS,
    _max_iterations,
    _trigger_webhook,
    run_pipeline,
)

_FAKE_SCHEMA = OntologySchema(
    namespace="http://www.example.com/genealogy.owl#",
    classes=(),
    datatype_properties=(),
    object_properties=(),
)


class _SuccessfulResponse:
    def raise_for_status(self) -> None:
        return None


class _PipelineStorage:
    def __init__(self) -> None:
        self.job = {
            "job_id": "job-1",
            "status": JobStatus.Pending.value,
            "input_text": "Jane Doe married John Doe in 1945.",
            "ontology_path": "ontology/family_extended.ttl",
            "current_iteration": 0,
            "max_iterations": DEFAULT_MAX_ITERATIONS,
            "last_error": None,
            "graph_turtle": None,
            "passed_validation": False,
            "webhook_url": None,
        }
        self.statuses: list[str] = []
        self.iterations: list[int] = []
        self.saved_graphs: list[dict[str, object]] = []
        self.iteration_details: list[dict[str, object]] = []

    def get_job(self, _job_id: str) -> dict[str, object]:
        return self.job

    def update_job_status(
        self,
        _job_id: str,
        status: JobStatus,
        last_error: str | None = None,
    ) -> None:
        self.job["status"] = status.value
        self.job["last_error"] = last_error
        self.statuses.append(status.value)

    def update_job_iteration(self, _job_id: str, current_iteration: int) -> None:
        self.job["current_iteration"] = current_iteration
        self.iterations.append(current_iteration)

    def add_iteration_detail(
        self,
        _job_id: str,
        iteration_number: int,
        violations: list[str],
        llm_reasoning: str,
        triples_before: int,
        triples_after: int,
    ) -> None:
        self.iteration_details.append(
            {
                "iteration_number": iteration_number,
                "violations": violations,
                "llm_reasoning": llm_reasoning,
                "triples_before": triples_before,
                "triples_after": triples_after,
            }
        )

    def save_final_graph(
        self,
        _job_id: str,
        graph_turtle: str,
        passed_validation: bool,
    ) -> None:
        self.job["graph_turtle"] = graph_turtle
        self.job["passed_validation"] = passed_validation
        self.saved_graphs.append(
            {
                "graph_turtle": graph_turtle,
                "passed_validation": passed_validation,
            }
        )

    def set_webhook_delivered(self, _job_id: str) -> None:
        raise AssertionError("No webhook should be delivered in these tests")


def _install_pipeline_storage(monkeypatch, storage: _PipelineStorage) -> None:
    monkeypatch.setattr("tasks.pipeline_task.database.get_job", storage.get_job)
    monkeypatch.setattr("tasks.pipeline_task.database.update_job_status", storage.update_job_status)
    monkeypatch.setattr(
        "tasks.pipeline_task.database.update_job_iteration",
        storage.update_job_iteration,
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.database.add_iteration_detail",
        storage.add_iteration_detail,
    )
    monkeypatch.setattr("tasks.pipeline_task.database.save_final_graph", storage.save_final_graph)
    monkeypatch.setattr(
        "tasks.pipeline_task.database.set_webhook_delivered",
        storage.set_webhook_delivered,
    )


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


def test_run_pipeline_maps_generic_extractions_before_building(monkeypatch) -> None:
    storage = _PipelineStorage()
    _install_pipeline_storage(monkeypatch, storage)
    monkeypatch.setattr(
        "tasks.pipeline_task.load_ontology_schema",
        lambda _path: _FAKE_SCHEMA,
    )
    generic_extractions = {
        "entities": [
            {
                "id": "john_1900",
                "label": "John",
                "type": "Person",
                "aliases": [],
                "attributes": {},
            },
            {
                "id": "jane_1925",
                "label": "Jane",
                "type": "Person",
                "aliases": [],
                "attributes": {},
            },
        ],
        "relations": [
            {
                "subject": "jane_1925",
                "object": "john_1900",
                "relation_phrase": "married to",
                "qualifiers": {"year": 1945, "note": None},
            }
        ],
    }
    mapped_extractions = {
        "entities": generic_extractions["entities"],
        "relations": [
            {"subject": "jane_1925", "predicate": "spouseOf", "object": "john_1900"}
        ],
    }
    extraction_inputs: list[tuple[str, OntologySchema]] = []
    mapping_inputs: list[tuple[dict[str, object], OntologySchema]] = []
    builder_inputs: list[tuple[dict[str, object], OntologySchema]] = []

    def fake_extraction(text, schema):
        extraction_inputs.append((text, schema))
        return generic_extractions

    def fake_mapping(extractions, schema):
        mapping_inputs.append((extractions, schema))
        assert extractions == generic_extractions
        return OntologyMappingResult(
            entities=mapped_extractions["entities"],
            relations=mapped_extractions["relations"],
            unmapped_relations=(),
        )

    def fake_builder(extractions, schema):
        builder_inputs.append((extractions, schema))
        return KGBuilderResult(
            turtle_graph=(
                "@prefix fhkb: <http://www.example.com/genealogy.owl#> .\n"
                "fhkb:jane_1925 a fhkb:Person .\n"
            ),
            dangling_references=(),
        )

    monkeypatch.setattr("tasks.pipeline_task.extraction_agent", fake_extraction)
    monkeypatch.setattr("tasks.pipeline_task.ontology_mapping_agent_with_diagnostics", fake_mapping)
    monkeypatch.setattr("tasks.pipeline_task.kg_builder_agent_with_diagnostics", fake_builder)
    monkeypatch.setattr(
        "tasks.pipeline_task.validation_agent",
        lambda _graph: {"conforms": True, "violations": []},
    )

    run_pipeline.run("job-1")

    assert extraction_inputs == [("Jane Doe married John Doe in 1945.", _FAKE_SCHEMA)]
    assert mapping_inputs == [(generic_extractions, _FAKE_SCHEMA)]
    assert builder_inputs == [(mapped_extractions, _FAKE_SCHEMA)]
    assert storage.statuses == [
        JobStatus.Extracting.value,
        JobStatus.Building.value,
        JobStatus.Validating.value,
        JobStatus.Complete.value,
    ]
    assert storage.iterations == [1]
    assert storage.saved_graphs == [
        {
            "graph_turtle": (
                "@prefix fhkb: <http://www.example.com/genealogy.owl#> .\n"
                "fhkb:jane_1925 a fhkb:Person .\n"
            ),
            "passed_validation": True,
        }
    ]


def test_run_pipeline_marks_job_error_when_ontology_path_missing(monkeypatch) -> None:
    storage = _PipelineStorage()
    storage.job["ontology_path"] = None
    _install_pipeline_storage(monkeypatch, storage)
    monkeypatch.delenv("DEFAULT_ONTOLOGY_PATH", raising=False)

    run_pipeline.run("job-1")

    assert storage.statuses == [JobStatus.Error.value]
    assert storage.job["last_error"] is not None


def test_run_pipeline_marks_job_error_when_ontology_schema_fails_to_load(monkeypatch) -> None:
    storage = _PipelineStorage()
    _install_pipeline_storage(monkeypatch, storage)

    def fail_load(_path):
        raise OntologySchemaError("could not parse ontology file")

    monkeypatch.setattr("tasks.pipeline_task.load_ontology_schema", fail_load)

    run_pipeline.run("job-1")

    assert storage.statuses == [JobStatus.Error.value]
    assert storage.job["last_error"] == "could not parse ontology file"


def test_run_pipeline_marks_job_error_when_ontology_mapping_fails(monkeypatch) -> None:
    storage = _PipelineStorage()
    _install_pipeline_storage(monkeypatch, storage)
    monkeypatch.setattr(
        "tasks.pipeline_task.load_ontology_schema",
        lambda _path: _FAKE_SCHEMA,
    )
    builder_called = False

    def fail_mapping(_extractions, _schema):
        raise OntologyMappingAgentError("mapping unavailable")

    def fake_builder(_extractions, _schema):
        nonlocal builder_called
        builder_called = True
        raise AssertionError("Builder must not run after mapping failure")

    monkeypatch.setattr(
        "tasks.pipeline_task.extraction_agent",
        lambda _text, _schema: {"entities": [], "relations": []},
    )
    monkeypatch.setattr("tasks.pipeline_task.ontology_mapping_agent_with_diagnostics", fail_mapping)
    monkeypatch.setattr("tasks.pipeline_task.kg_builder_agent_with_diagnostics", fake_builder)

    run_pipeline.run("job-1")

    assert builder_called is False
    assert storage.statuses == [
        JobStatus.Extracting.value,
        JobStatus.Building.value,
        JobStatus.Error.value,
    ]
    assert storage.job["last_error"] == "mapping unavailable"
    assert storage.saved_graphs == []