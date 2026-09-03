from datetime import datetime
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field, HttpUrl


class JobStatus(str, Enum):
    Pending = "Pending"
    Extracting = "Extracting"
    Building = "Building"
    Validating = "Validating"
    Repairing = "Repairing"
    Complete = "Complete"
    Error = "Error"
    MaxIterationsReached = "MaxIterationsReached"


class JobCreateRequest(BaseModel):
    text: str = Field(..., min_length=10)
    question: str = Field(..., min_length=1)
    webhook_url: Optional[HttpUrl] = None
    ontology_path: Optional[str] = Field(
        default=None,
        description=(
            "Path to the OWL/TTL ontology file to extract against. If omitted, "
            "falls back to the DEFAULT_ONTOLOGY_PATH environment variable."
        ),
    )


class JobCreateResponse(BaseModel):
    job_id: str
    status: JobStatus
    created_at: datetime


class JobStatusResponse(BaseModel):
    job_id: str
    status: JobStatus
    current_iteration: int
    max_iterations: int
    last_error: Optional[str]
    created_at: datetime
    updated_at: datetime


class IterationDetail(BaseModel):
    iteration_number: int
    violations: list[str]
    llm_reasoning: str
    triples_before: int
    triples_after: int
    edit_log: list[dict[str, Any]] = Field(default_factory=list)
    unresolved_violation_fingerprints: list[str] = Field(default_factory=list)
    timestamp: datetime


class JobIterationsResponse(BaseModel):
    job_id: str
    iterations: list[IterationDetail]


class GraphFormat(str, Enum):
    turtle = "turtle"
    json_ld = "json_ld"
    rdf_xml = "rdf_xml"


class JobGraphResponse(BaseModel):
    job_id: str
    format: GraphFormat
    graph_content: str
    triple_count: int
    passed_validation: bool
