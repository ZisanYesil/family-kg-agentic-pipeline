from __future__ import annotations

import httpx
from rdflib import Graph

from agents.kg_builder_agent import DanglingRelationReference, KGBuilderResult
from agents.ontology_mapping_agent import (
    OntologyMappingAgentError,
    OntologyMappingResult,
    UnmappedRelation,
)
from agents.feedback_agent import FeedbackAgentError
from agents.validation_agent import ValidationAgentError
from feedback.models import FeedbackPlan
from api.models.job import JobStatus
from ontology.schema_loader import (
    DatatypeProperty,
    ObjectProperty,
    OntologyClass,
    OntologySchema,
    OntologySchemaError,
)
from tasks.pipeline_task import (
    DEFAULT_MAX_ITERATIONS,
    DEFAULT_WEBHOOK_MAX_ATTEMPTS,
    _max_iterations,
    _trigger_webhook,
    run_pipeline,
)
from utils.rdf import parse_turtle_graph
from validation.models import (
    ValidationResult,
    ValidationViolation,
    ViolationKind,
    ViolationSource,
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
        **metadata,
    ) -> None:
        self.iteration_details.append(
            {
                "iteration_number": iteration_number,
                "violations": violations,
                "llm_reasoning": llm_reasoning,
                "triples_before": triples_before,
                "triples_after": triples_after,
                **metadata,
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


def _unresolved_plan(violations) -> FeedbackPlan:
    return FeedbackPlan.model_validate(
        {
            "reasoning": "No safe source-grounded repair was found.",
            "repairs": [
                {
                    "violation_fingerprint": violation.fingerprint,
                    "reasoning": "The available evidence is insufficient.",
                    "operations": [],
                }
                for violation in violations
            ],
        }
    )


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
    assert storage.saved_graphs[0]["passed_validation"] is True
    assert set(parse_turtle_graph(storage.saved_graphs[0]["graph_turtle"])) == set(
        parse_turtle_graph(
            "@prefix fhkb: <http://www.example.com/genealogy.owl#> .\n"
            "fhkb:jane_1925 a fhkb:Person .\n"
        )
    )


def test_run_pipeline_passes_dangling_reference_to_feedback_and_blocks_completion(
    monkeypatch,
) -> None:
    storage = _PipelineStorage()
    _install_pipeline_storage(monkeypatch, storage)
    schema = OntologySchema(
        namespace="http://example.com/family#",
        classes=(),
        datatype_properties=(),
        object_properties=(
            ObjectProperty(
                local_name="hasFather",
                uri="http://example.com/family#hasFather",
                domain_class="Person",
                range_class="Man",
            ),
        ),
    )
    turtle = (
        "@prefix ex: <http://example.com/family#> .\n"
        "ex:known_child ex:hasFather ex:unknown_father .\n"
    )
    dangling = DanglingRelationReference(
        role="object",
        entity_id="unknown_father",
        predicate="hasFather",
        subject_id="known_child",
        object_id="unknown_father",
    )
    feedback_inputs = []

    monkeypatch.setenv("MAX_ITERATIONS", "2")
    monkeypatch.setattr("tasks.pipeline_task.load_ontology_schema", lambda _path: schema)
    monkeypatch.setattr(
        "tasks.pipeline_task.extraction_agent",
        lambda _text, _schema: {"entities": [], "relations": []},
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.ontology_mapping_agent_with_diagnostics",
        lambda _extractions, _schema: OntologyMappingResult(
            entities=[],
            relations=[],
            unmapped_relations=(),
        ),
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.kg_builder_agent_with_diagnostics",
        lambda _extractions, _schema: KGBuilderResult(
            turtle_graph=turtle,
            dangling_references=(dangling,),
        ),
    )
    def fake_feedback(_graph, violations, _schema, _source_text):
        feedback_inputs.append(violations)
        return _unresolved_plan(violations)

    monkeypatch.setattr("tasks.pipeline_task.feedback_agent", fake_feedback)

    run_pipeline.run("job-1")

    assert len(feedback_inputs) == 1
    assert any(item.kind == ViolationKind.DANGLING_REFERENCE for item in feedback_inputs[0])
    assert any(item.expected == "Man" for item in feedback_inputs[0])
    assert JobStatus.Complete.value not in storage.statuses
    assert storage.statuses[-1] == JobStatus.Error.value
    assert storage.saved_graphs[-1]["passed_validation"] is False


def test_run_pipeline_passes_unmapped_relation_to_feedback_and_blocks_completion(
    monkeypatch,
) -> None:
    storage = _PipelineStorage()
    _install_pipeline_storage(monkeypatch, storage)
    schema = OntologySchema(
        namespace="http://example.com/family#",
        classes=(),
        datatype_properties=(),
        object_properties=(
            ObjectProperty(
                local_name="hasFather",
                uri="http://example.com/family#hasFather",
                domain_class="Person",
                range_class="Man",
            ),
        ),
    )
    entities = [
        {"id": "known_child", "type": "Person"},
        {"id": "known_father", "type": "Man"},
    ]
    unmapped = UnmappedRelation(
        subject="known_child",
        object="known_father",
        relation_phrase="father",
        reason="relation_phrase did not match any ontology predicate",
    )
    turtle = (
        "@prefix ex: <http://example.com/family#> .\n"
        "ex:known_child a ex:Person .\n"
        "ex:known_father a ex:Man .\n"
    )
    feedback_inputs = []

    monkeypatch.setenv("MAX_ITERATIONS", "2")
    monkeypatch.setattr("tasks.pipeline_task.load_ontology_schema", lambda _path: schema)
    monkeypatch.setattr(
        "tasks.pipeline_task.extraction_agent",
        lambda _text, _schema: {"entities": entities, "relations": []},
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.ontology_mapping_agent_with_diagnostics",
        lambda _extractions, _schema: OntologyMappingResult(
            entities=entities,
            relations=[],
            unmapped_relations=(unmapped,),
        ),
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.kg_builder_agent_with_diagnostics",
        lambda _extractions, _schema: KGBuilderResult(
            turtle_graph=turtle,
            dangling_references=(),
        ),
    )
    def fake_feedback(_graph, violations, _schema, _source_text):
        feedback_inputs.append(violations)
        return _unresolved_plan(violations)

    monkeypatch.setattr("tasks.pipeline_task.feedback_agent", fake_feedback)

    run_pipeline.run("job-1")

    assert len(feedback_inputs) == 1
    assert any(item.kind == ViolationKind.UNMAPPED_RELATION for item in feedback_inputs[0])
    assert any("http://example.com/family#hasFather" in (item.expected or "") for item in feedback_inputs[0])
    assert JobStatus.Complete.value not in storage.statuses
    assert storage.statuses[-1] == JobStatus.Error.value


def test_run_pipeline_clears_unmapped_diagnostic_after_feedback_adds_candidate_triple(
    monkeypatch,
) -> None:
    storage = _PipelineStorage()
    _install_pipeline_storage(monkeypatch, storage)
    schema = OntologySchema(
        namespace="http://example.com/family#",
        classes=(),
        datatype_properties=(),
        object_properties=(
            ObjectProperty(
                local_name="hasFather",
                uri="http://example.com/family#hasFather",
                domain_class="Person",
                range_class="Man",
            ),
        ),
    )
    entities = [
        {"id": "known_child", "type": "Person"},
        {"id": "known_father", "type": "Man"},
    ]
    unmapped = UnmappedRelation(
        subject="known_child",
        object="known_father",
        relation_phrase="father",
        reason="relation_phrase did not match any ontology predicate",
    )
    initial_turtle = (
        "@prefix ex: <http://example.com/family#> .\n"
        "ex:known_child a ex:Person .\n"
        "ex:known_father a ex:Man .\n"
    )
    repaired_turtle = (
        initial_turtle
        + "ex:known_child ex:hasFather ex:known_father .\n"
    )
    pipeline_parse_calls: list[str] = []

    def counted_pipeline_parse(turtle: str) -> Graph:
        pipeline_parse_calls.append(turtle)
        return parse_turtle_graph(turtle)

    monkeypatch.setenv("MAX_ITERATIONS", "3")
    monkeypatch.setattr(
        "tasks.pipeline_task.parse_turtle_graph",
        counted_pipeline_parse,
    )
    monkeypatch.setattr("tasks.pipeline_task.load_ontology_schema", lambda _path: schema)
    monkeypatch.setattr(
        "tasks.pipeline_task.extraction_agent",
        lambda _text, _schema: {"entities": entities, "relations": []},
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.ontology_mapping_agent_with_diagnostics",
        lambda _extractions, _schema: OntologyMappingResult(
            entities=entities,
            relations=[],
            unmapped_relations=(unmapped,),
        ),
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.kg_builder_agent_with_diagnostics",
        lambda _extractions, _schema: KGBuilderResult(
            turtle_graph=initial_turtle,
            dangling_references=(),
        ),
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.feedback_agent",
        lambda _graph, violations, _schema, _source_text: FeedbackPlan.model_validate(
            {
                "reasoning": "Mapped the source-supported father relation.",
                "repairs": [
                    {
                        "violation_fingerprint": violation.fingerprint,
                        "reasoning": "The father relation is stated in the source.",
                        "operations": [
                            {
                                "operation": "add_triple",
                                "subject": "http://example.com/family#known_child",
                                "predicate": "http://example.com/family#hasFather",
                                "object": {"kind": "iri", "value": "http://example.com/family#known_father"},
                            }
                        ],
                    }
                    for violation in violations
                ],
            }
        ),
    )

    run_pipeline.run("job-1")

    assert storage.iterations == [1, 2]
    assert pipeline_parse_calls == [initial_turtle]
    assert storage.statuses[-1] == JobStatus.Complete.value
    assert storage.saved_graphs[-1]["passed_validation"] is True
    assert set(parse_turtle_graph(storage.saved_graphs[-1]["graph_turtle"])) == set(
        parse_turtle_graph(repaired_turtle)
    )
    assert storage.iteration_details[0]["violations"]
    assert storage.iteration_details[0]["edit_log"][0]["operation"] == "add_triple"
    assert storage.iteration_details[0]["unresolved_violation_fingerprints"] == []
    assert storage.iteration_details[1]["violations"] == []


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


def test_run_pipeline_marks_job_error_when_validation_infrastructure_fails(
    monkeypatch,
) -> None:
    storage = _PipelineStorage()
    _install_pipeline_storage(monkeypatch, storage)
    monkeypatch.setattr(
        "tasks.pipeline_task.load_ontology_schema",
        lambda _path: _FAKE_SCHEMA,
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.extraction_agent",
        lambda _text, _schema: {"entities": [], "relations": []},
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.ontology_mapping_agent_with_diagnostics",
        lambda _extractions, _schema: OntologyMappingResult(
            entities=[],
            relations=[],
            unmapped_relations=(),
        ),
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.kg_builder_agent_with_diagnostics",
        lambda _extractions, _schema: KGBuilderResult(
            turtle_graph="",
            dangling_references=(),
        ),
    )

    def fail_validation(_graph, _schema, **_kwargs):
        raise ValidationAgentError("SHACL engine unavailable")

    monkeypatch.setattr("tasks.pipeline_task.validation_agent", fail_validation)

    run_pipeline.run("job-1")

    assert storage.statuses[-2:] == [
        JobStatus.Validating.value,
        JobStatus.Error.value,
    ]
    assert storage.job["last_error"] == "SHACL engine unavailable"
    assert storage.saved_graphs == []


def test_run_pipeline_real_shacl_violation_blocks_completion_and_reaches_feedback(
    monkeypatch,
) -> None:
    storage = _PipelineStorage()
    _install_pipeline_storage(monkeypatch, storage)
    schema = OntologySchema(
        namespace="http://example.com/mixed#",
        classes=(
            OntologyClass(
                local_name="Car",
                uri="http://example.com/mixed#Car",
            ),
        ),
        datatype_properties=(
            DatatypeProperty(
                local_name="modelYear",
                uri="http://example.com/mixed#modelYear",
                domain_class="Car",
                range_type="integer",
            ),
        ),
        object_properties=(),
    )
    invalid_turtle = (
        "@prefix ex: <http://example.com/mixed#> .\n"
        "ex:car a ex:Car ; ex:modelYear \"recent\" .\n"
    )
    feedback_inputs = []

    monkeypatch.setenv("MAX_ITERATIONS", "2")
    monkeypatch.setattr("tasks.pipeline_task.load_ontology_schema", lambda _path: schema)
    monkeypatch.setattr(
        "tasks.pipeline_task.extraction_agent",
        lambda _text, _schema: {"entities": [], "relations": []},
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.ontology_mapping_agent_with_diagnostics",
        lambda _extractions, _schema: OntologyMappingResult(
            entities=[],
            relations=[],
            unmapped_relations=(),
        ),
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.kg_builder_agent_with_diagnostics",
        lambda _extractions, _schema: KGBuilderResult(
            turtle_graph=invalid_turtle,
            dangling_references=(),
        ),
    )

    def unchanged_feedback(_graph, violations, _schema, _source_text):
        feedback_inputs.append(violations)
        return _unresolved_plan(violations)

    monkeypatch.setattr("tasks.pipeline_task.feedback_agent", unchanged_feedback)

    run_pipeline.run("job-1")

    assert len(feedback_inputs) == 1
    assert any(violation.kind == ViolationKind.SHACL for violation in feedback_inputs[0])
    assert any("DatatypeConstraintComponent" in (violation.constraint_component or "") for violation in feedback_inputs[0])
    assert JobStatus.Complete.value not in storage.statuses
    assert storage.statuses[-1] == JobStatus.Error.value
    assert storage.saved_graphs[-1]["passed_validation"] is False


def test_run_pipeline_rejects_string_feedback_graph_and_passes_independent_copy(
    monkeypatch,
) -> None:
    storage = _PipelineStorage()
    _install_pipeline_storage(monkeypatch, storage)
    source_turtle = (
        "@prefix ex: <http://example.com/family#> .\n"
        "ex:child a ex:Person .\n"
    )
    validation_graphs: list[Graph] = []
    feedback_graphs: list[Graph] = []
    finding = ValidationViolation(
        kind=ViolationKind.SHACL,
        source=ViolationSource.SHACL_GENERATOR,
        focus_node="http://example.com/family#child",
        message="Needs repair",
    )

    monkeypatch.setattr(
        "tasks.pipeline_task.load_ontology_schema",
        lambda _path: _FAKE_SCHEMA,
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.extraction_agent",
        lambda _text, _schema: {"entities": [], "relations": []},
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.ontology_mapping_agent_with_diagnostics",
        lambda _extractions, _schema: OntologyMappingResult(
            entities=[],
            relations=[],
            unmapped_relations=(),
        ),
    )
    monkeypatch.setattr(
        "tasks.pipeline_task.kg_builder_agent_with_diagnostics",
        lambda _extractions, _schema: KGBuilderResult(
            turtle_graph=source_turtle,
            dangling_references=(),
        ),
    )

    def fake_validation(graph: Graph, _schema, **_kwargs) -> ValidationResult:
        validation_graphs.append(graph)
        return ValidationResult(violations=(finding,))

    def invalid_feedback(graph, _violations, _schema, _source_text):
        feedback_graphs.append(graph)
        graph.remove((None, None, None))
        raise FeedbackAgentError("Invalid feedback response")

    monkeypatch.setattr("tasks.pipeline_task.validation_agent", fake_validation)
    monkeypatch.setattr("tasks.pipeline_task.feedback_agent", invalid_feedback)

    run_pipeline.run("job-1")

    assert len(validation_graphs) == 1
    assert len(feedback_graphs) == 1
    assert feedback_graphs[0] is not validation_graphs[0]
    assert len(validation_graphs[0]) == 1
    assert storage.statuses[-1] == JobStatus.Error.value
    assert storage.job["last_error"] == "Invalid feedback response"
    assert storage.saved_graphs == []
