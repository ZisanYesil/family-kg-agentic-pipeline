import os
from typing import Any
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query, status
import structlog

from api.models.job import (
    GraphFormat,
    JobCreateRequest,
    JobCreateResponse,
    JobGraphResponse,
    JobIterationsResponse,
    JobStatus,
    JobStatusResponse,
)
from api.task_queue import dispatch_extraction_job
from storage import database
from utils.rdf import TurtleParseError, parse_turtle_graph, serialize_graph

router = APIRouter(prefix="/jobs", tags=["jobs"])
logger = structlog.get_logger(__name__)


def get_storage() -> Any:
    return database


@router.post("", response_model=JobCreateResponse, status_code=status.HTTP_202_ACCEPTED)
def create_kg_extraction_job(
    request: JobCreateRequest,
    db: Any = Depends(get_storage),
) -> JobCreateResponse:
    """Create a knowledge graph extraction job and queue the async workflow."""
    job_id = str(uuid4())
    max_iterations = int(os.getenv("MAX_ITERATIONS", "10"))
    webhook_url = str(request.webhook_url) if request.webhook_url else None

    ontology_path = request.ontology_path or os.getenv("DEFAULT_ONTOLOGY_PATH")
    if not ontology_path:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=(
                "ontology_path was not provided and DEFAULT_ONTOLOGY_PATH is not set"
            ),
        )

    db.create_job(
        job_id=job_id,
        input_text=request.text,
        ontology_path=ontology_path,
        max_iterations=max_iterations,
        webhook_url=webhook_url,
    )
    dispatch_extraction_job(job_id)

    job = db.get_job(job_id)
    if job is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Job was created but could not be read back",
        )

    return JobCreateResponse(
        job_id=job_id,
        status=JobStatus(job["status"]),
        created_at=job["created_at"],
    )


@router.get("/{job_id}/status", response_model=JobStatusResponse)
def get_kg_extraction_status(
    job_id: str,
    db: Any = Depends(get_storage),
) -> JobStatusResponse:
    """Return the current lifecycle state and latest validation feedback for a job."""
    job = db.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return JobStatusResponse(
        job_id=job["job_id"],
        status=JobStatus(job["status"]),
        current_iteration=job["current_iteration"],
        max_iterations=job["max_iterations"],
        last_error=job["last_error"],
        created_at=job["created_at"],
        updated_at=job["updated_at"],
    )


@router.get("/{job_id}/graph", response_model=JobGraphResponse)
def get_validated_graph(
    job_id: str,
    format: GraphFormat = Query(default=GraphFormat.turtle),
    db: Any = Depends(get_storage),
) -> JobGraphResponse:
    """Return the generated knowledge graph in the requested RDF serialization format."""
    job = db.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    job_status = JobStatus(job["status"])
    if job_status != JobStatus.Complete:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Validated graph is not available while job status is {job_status.value}",
        )

    graph_content = job["graph_turtle"] or ""
    try:
        graph = parse_turtle_graph(graph_content)
    except TurtleParseError as exc:
        logger.exception("graph_parse_failed", job_id=job_id, error=str(exc))
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Stored graph_turtle is not valid Turtle and cannot be serialized",
        ) from exc

    return JobGraphResponse(
        job_id=job_id,
        format=format,
        graph_content=serialize_graph(graph, format),
        triple_count=len(graph),
        passed_validation=job["passed_validation"],
    )


@router.get("/{job_id}/iterations", response_model=JobIterationsResponse)
def get_iteration_history(
    job_id: str,
    db: Any = Depends(get_storage),
) -> JobIterationsResponse:
    """Return the recorded validation and repair history for a job."""
    job = db.get_job(job_id)
    if job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    iterations = db.get_iterations(job_id)
    return JobIterationsResponse(job_id=job_id, iterations=iterations)
