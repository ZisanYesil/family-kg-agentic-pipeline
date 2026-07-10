import os
from collections.abc import Mapping
from typing import Any, Optional

import httpx
import structlog

from agents.extraction_agent import ExtractionAgentError, extraction_agent
from agents.kg_builder_agent import KGBuilderError, kg_builder_agent, kg_builder_agent_with_diagnostics
from agents.ontology_mapping_agent import (
    OntologyMappingAgentError,
    ontology_mapping_agent_with_diagnostics,
)
from api.models.job import JobStatus
from celery_app import celery_app
from storage import database
from utils.rdf import count_turtle_triples

logger = structlog.get_logger(__name__)

DEFAULT_MAX_ITERATIONS = 10
MAX_ITERATIONS_ENV = "MAX_ITERATIONS"
DEFAULT_WEBHOOK_TIMEOUT_SECONDS = 10
DEFAULT_WEBHOOK_MAX_ATTEMPTS = 3
WEBHOOK_TIMEOUT_ENV = "WEBHOOK_TIMEOUT_SECONDS"
WEBHOOK_MAX_ATTEMPTS_ENV = "WEBHOOK_MAX_ATTEMPTS"


def validation_agent(turtle_graph: str) -> dict[str, Any]:
    """Placeholder Validation Agent that always returns a conforming graph."""
    return {"conforms": True, "violations": []}


def feedback_agent(turtle_graph: str, violations: list[str]) -> dict[str, str]:
    """Placeholder Feedback Agent that returns the graph unchanged."""
    return {"reasoning": "", "corrected_graph": turtle_graph}


def _max_iterations(env: Optional[Mapping[str, str]] = None) -> int:
    return _positive_int_env(MAX_ITERATIONS_ENV, DEFAULT_MAX_ITERATIONS, env)


def _positive_int_env(
    env_var: str,
    default: int,
    env: Optional[Mapping[str, str]] = None,
) -> int:
    source = env if env is not None else os.environ
    raw_value = source.get(env_var)
    if raw_value is None:
        return default

    try:
        value = int(raw_value)
    except ValueError:
        logger.warning(
            "invalid_positive_int_env",
            env_var=env_var,
            value=raw_value,
            default=default,
        )
        return default

    if value < 1:
        logger.warning(
            "invalid_positive_int_env",
            env_var=env_var,
            value=raw_value,
            default=default,
        )
        return default

    return value


def _transition(
    job_id: str,
    from_status: JobStatus,
    to_status: JobStatus,
    last_error: Optional[str] = None,
) -> JobStatus:
    database.update_job_status(job_id, to_status, last_error=last_error)
    logger.info(
        "job_status_transition",
        job_id=job_id,
        from_status=from_status.value,
        to_status=to_status.value,
    )
    return to_status


def _trigger_webhook(job: dict[str, Any]) -> None:
    webhook_url = job.get("webhook_url")
    if not webhook_url:
        return

    timeout_seconds = _positive_int_env(WEBHOOK_TIMEOUT_ENV, DEFAULT_WEBHOOK_TIMEOUT_SECONDS)
    max_attempts = _positive_int_env(WEBHOOK_MAX_ATTEMPTS_ENV, DEFAULT_WEBHOOK_MAX_ATTEMPTS)
    payload = {
        "job_id": job["job_id"],
        "status": job["status"],
        "passed_validation": job["passed_validation"],
        "current_iteration": job["current_iteration"],
        "last_error": job["last_error"],
    }

    last_error: Optional[Exception] = None
    for attempt in range(1, max_attempts + 1):
        try:
            response = httpx.post(webhook_url, json=payload, timeout=timeout_seconds)
            response.raise_for_status()
            break
        except httpx.HTTPError as exc:
            last_error = exc
            logger.warning(
                "webhook_delivery_attempt_failed",
                job_id=job["job_id"],
                webhook_url=webhook_url,
                attempt=attempt,
                max_attempts=max_attempts,
                error=str(exc),
            )
        except Exception as exc:
            logger.exception(
                "webhook_delivery_failed",
                job_id=job["job_id"],
                webhook_url=webhook_url,
                attempt=attempt,
                max_attempts=max_attempts,
                error=str(exc),
            )
            return
    else:
        logger.error(
            "webhook_delivery_failed",
            job_id=job["job_id"],
            webhook_url=webhook_url,
            attempt_count=max_attempts,
            error=str(last_error),
        )
        return

    try:
        database.set_webhook_delivered(job["job_id"])
        logger.info(
            "webhook_delivered",
            job_id=job["job_id"],
            webhook_url=webhook_url,
            attempt=attempt,
        )
    except Exception as exc:
        logger.exception(
            "webhook_mark_delivered_failed_after_delivery",
            job_id=job["job_id"],
            webhook_url=webhook_url,
            error=str(exc),
        )


def _finish(job_id: str) -> None:
    job = database.get_job(job_id)
    if job is None:
        logger.error("cannot_trigger_webhook_for_missing_job", job_id=job_id)
        return
    _trigger_webhook(job)


@celery_app.task(
    name="tasks.pipeline_task.run_pipeline",
    bind=True,
    autoretry_for=(Exception,),
    max_retries=3,
    retry_kwargs={"countdown": 5},
)
def run_pipeline(self: Any, job_id: str) -> None:
    """Run the agentic KG pipeline with SHACL iteration retries and Celery API retries separated."""
    current_status = JobStatus.Pending

    try:
        job = database.get_job(job_id)
        if job is None:
            logger.error("pipeline_job_not_found", job_id=job_id)
            return

        current_status = JobStatus(job["status"])
        max_iterations = _max_iterations()
        previous_violations: Optional[list[str]] = None

        current_status = _transition(job_id, current_status, JobStatus.Extracting)
        try:
            extractions = extraction_agent(job["input_text"])
        except ExtractionAgentError as exc:
            current_status = _transition(job_id, current_status, JobStatus.Error, last_error=str(exc))
            logger.exception("extraction_agent_failed", job_id=job_id, error=str(exc))
            _finish(job_id)
            return

        current_status = _transition(job_id, current_status, JobStatus.Building)
        try:
            ontology_mapping_result = ontology_mapping_agent_with_diagnostics(extractions)
            if ontology_mapping_result.unmapped_relations:
                logger.warning(
                    "ontology_mapping_unmapped_relations",
                    job_id=job_id,
                    unmapped_relation_count=len(ontology_mapping_result.unmapped_relations),
                    unmapped_relations=ontology_mapping_result.unmapped_relations,
                )

            mapped_extractions = {
                "entities": ontology_mapping_result.entities,
                "relations": ontology_mapping_result.relations,
                "marriages": ontology_mapping_result.marriages,
            }
            kg_builder_result = kg_builder_agent_with_diagnostics(mapped_extractions)
            turtle_graph = kg_builder_result.turtle_graph
            if kg_builder_result.dangling_references or kg_builder_result.dangling_marriage_references:
                logger.warning(
                    "kg_builder_dangling_references",
                    job_id=job_id,
                    dangling_reference_count=len(kg_builder_result.dangling_references),
                    dangling_marriage_reference_count=len(
                        kg_builder_result.dangling_marriage_references
                    ),
                    dangling_references=kg_builder_result.dangling_references,
                    dangling_marriage_references=kg_builder_result.dangling_marriage_references,
                )
        except OntologyMappingAgentError as exc:
            current_status = _transition(job_id, current_status, JobStatus.Error, last_error=str(exc))
            logger.exception("ontology_mapping_agent_failed", job_id=job_id, error=str(exc))
            _finish(job_id)
            return
        except KGBuilderError as exc:
            current_status = _transition(job_id, current_status, JobStatus.Error, last_error=str(exc))
            logger.exception("kg_builder_agent_failed", job_id=job_id, error=str(exc))
            _finish(job_id)
            return

        # Iterations operate on the current graph. Feedback mutates that graph;
        # extraction/building should not restart unless the whole Celery task retries.
        for iteration_number in range(1, max_iterations + 1):
            database.update_job_iteration(job_id, iteration_number)
            triples_before = count_turtle_triples(turtle_graph)

            current_status = _transition(job_id, current_status, JobStatus.Validating)
            validation_result = validation_agent(turtle_graph)
            violations = list(validation_result.get("violations", []))
            conforms = bool(validation_result.get("conforms", False))

            if conforms:
                triples_after = count_turtle_triples(turtle_graph)
                database.add_iteration_detail(
                    job_id,
                    iteration_number,
                    violations,
                    "",
                    triples_before,
                    triples_after,
                )
                logger.info(
                    "pipeline_iteration",
                    job_id=job_id,
                    iteration_number=iteration_number,
                    violation_count=len(violations),
                    triples_before=triples_before,
                    triples_after=triples_after,
                )
                database.save_final_graph(job_id, turtle_graph, passed_validation=True)
                current_status = _transition(job_id, current_status, JobStatus.Complete)
                _finish(job_id)
                return

            if previous_violations == violations:
                reason = "Plateau detected: two consecutive iterations produced identical validation reports"
                database.add_iteration_detail(
                    job_id,
                    iteration_number,
                    violations,
                    reason,
                    triples_before,
                    triples_before,
                )
                logger.info(
                    "pipeline_iteration",
                    job_id=job_id,
                    iteration_number=iteration_number,
                    violation_count=len(violations),
                    triples_before=triples_before,
                    triples_after=triples_before,
                )
                database.save_final_graph(job_id, turtle_graph, passed_validation=False)
                current_status = _transition(job_id, current_status, JobStatus.Error, last_error=reason)
                logger.error("pipeline_plateau_detected", job_id=job_id, iteration_number=iteration_number)
                _finish(job_id)
                return

            current_status = _transition(job_id, current_status, JobStatus.Repairing)
            feedback = feedback_agent(turtle_graph, violations)
            corrected_graph = feedback.get("corrected_graph", turtle_graph)
            reasoning = feedback.get("reasoning", "")
            triples_after = count_turtle_triples(corrected_graph)

            database.add_iteration_detail(
                job_id,
                iteration_number,
                violations,
                reasoning,
                triples_before,
                triples_after,
            )
            logger.info(
                "pipeline_iteration",
                job_id=job_id,
                iteration_number=iteration_number,
                violation_count=len(violations),
                triples_before=triples_before,
                triples_after=triples_after,
            )

            previous_violations = violations
            turtle_graph = corrected_graph

        reason = f"Maximum iteration limit reached ({max_iterations})"
        database.save_final_graph(job_id, turtle_graph, passed_validation=False)
        current_status = _transition(
            job_id,
            current_status,
            JobStatus.MaxIterationsReached,
            last_error=reason,
        )
        logger.warning("pipeline_max_iterations_reached", job_id=job_id, max_iterations=max_iterations)
        _finish(job_id)

    except Exception as exc:
        logger.exception(
            "pipeline_task_failed",
            job_id=job_id,
            error=str(exc),
            celery_retry=self.request.retries,
            celery_max_retries=self.max_retries,
        )
        if self.request.retries >= self.max_retries:
            _transition(job_id, current_status, JobStatus.Error, last_error=str(exc))
            logger.exception(
                "pipeline_task_marked_error_after_retries",
                job_id=job_id,
                error=str(exc),
            )
            _finish(job_id)
            return
        raise
