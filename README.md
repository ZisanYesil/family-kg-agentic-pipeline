# Family KG Agentic Pipeline

An agentic AI pipeline for extracting family relationships from unstructured text, converting them into ontology-grounded RDF, and exposing the workflow through an asynchronous API.

This README describes the current project state. Items that are part of the internship task but are not fully implemented yet are listed under [Future Work](#future-work).

## Current Status

Implemented:

- FastAPI REST API for creating extraction jobs, checking status, retrieving the generated graph, and reading iteration history.
- Celery + Redis asynchronous workflow.
- SQLite persistence for job state, generated Turtle graphs, iteration metadata, and webhook delivery state.
- LLM-driven Extraction Agent using OpenAI chat completions with a strict JSON schema.
- KG Builder Agent that converts structured extraction output into RDF/Turtle using the family ontology namespace.
- Extended ontology artifact and SHACL shapes for family relationship constraints.
- Dockerized API, worker, and Redis services.
- Structured JSON logging with `structlog`.
- Optional webhook callback when a job finishes.
- Unit tests for extraction, RDF generation, ontology namespace handling, SHACL shapes, API behavior, pipeline settings, and webhook retry behavior.

Not fully implemented yet:

- `validation_agent` currently returns success as a placeholder instead of running `pyshacl` in the pipeline.
- `feedback_agent` currently returns the graph unchanged instead of using an LLM to interpret validation errors and repair the graph.
- Evaluation/reporting metrics are not yet automated.

## Internship Task Coverage

The task asks for an agentic system that extracts family data from text, builds an ontology-consistent knowledge graph, validates it with OWL/SHACL, improves it iteratively, exposes it through an API, and documents architecture, usage, outputs, limitations, and future enhancements.

Current coverage:

| Requirement | Current state |
| --- | --- |
| Text processing and information extraction | Implemented in `agents/extraction_agent.py` with OpenAI structured JSON output. |
| RDF knowledge graph construction | Implemented in `agents/kg_builder_agent.py` using `rdflib`. |
| Ontology alignment | Uses `http://www.example.com/genealogy.owl#` family namespace, `ontology/family_extended.ttl`, and relationship-specific predicates. |
| Validation with OWL/SHACL | SHACL shapes exist in `shapes/family_shapes.ttl` and are tested, but the pipeline validation agent is still a placeholder. |
| Error-driven iterative improvement | Pipeline loop, status transitions, iteration storage, plateau detection, and max-iteration handling exist; actual validation/repair logic is future work. |
| Agentic architecture | Custom multi-agent pipeline with Extraction, KG Builder, Validation, and Feedback agent roles. |
| API exposure | Implemented with async job creation, status, graph retrieval, and iteration history endpoints. |
| Logging | Implemented with JSON structured logs. |
| Dockerization | Implemented with `Dockerfile` and `docker-compose.yml`. |
| Webhooks | Implemented as optional finish callback with retries. |
| Performance/evaluation report | Not automated yet; see Future Work. |

## Architecture

```text
Client
  |
  | POST /jobs
  v
FastAPI API
  |
  | create job in SQLite
  | enqueue Celery task
  v
Redis broker
  |
  v
Celery worker
  |
  | 1. Extraction Agent
  |    narrative text -> structured entities, relations, marriages
  |
  | 2. KG Builder Agent
  |    structured JSON -> RDF/Turtle
  |
  | 3. Validation Agent
  |    currently placeholder; intended to run SHACL/OWL validation
  |
  | 4. Feedback Agent
  |    currently placeholder; intended to repair graph from validation errors
  |
  | save graph, iteration details, status
  | optional webhook callback
  v
SQLite
```

### Agent Roles

**Extraction Agent**  
File: `agents/extraction_agent.py`

The extraction agent sends the input text to an OpenAI model and requires a strict JSON schema response with:

- `entities`: people with stable ids, labels, sex, birth/death years, and aliases.
- `relations`: direct family relations using the supported ontology predicates.
- `marriages`: marriage events represented separately from direct person-to-person relations.

Supported relation predicates:

- `hasFather`
- `hasMother`
- `hasBrother`
- `hasSister`
- `hasSon`
- `hasDaughter`
- `hasHusband`
- `hasWife`

**KG Builder Agent**  
File: `agents/kg_builder_agent.py`

The KG Builder Agent validates the extraction structure and generates RDF/Turtle. It:

- Emits `fhkb:Person` and `owl:NamedIndividual` for each person.
- Emits `rdfs:label`, `fhkb:hasSex`, `fhkb:hasBirthYear`, `fhkb:hasDeathYear`, and `fhkb:alsoKnownAs` when present.
- Emits direct family relation triples.
- Represents marriages as `fhkb:Marriage` individuals with `fhkb:hasMalePartner`, `fhkb:hasFemalePartner`, and `fhkb:hasMarriageYear`.
- Sanitizes entity ids into deterministic URI local names.
- Rejects unsupported predicates and conflicting functional year values.
- Logs dangling relation or marriage references without failing graph generation.

**Validation Agent**  
File: `tasks/pipeline_task.py`

Currently implemented as a placeholder:

```python
def validation_agent(turtle_graph: str) -> dict[str, Any]:
    return {"conforms": True, "violations": []}
```

The project already contains SHACL shapes in `shapes/family_shapes.ttl`, and tests verify them with `pyshacl`. The next implementation step is to call `pyshacl.validate` from this agent and return real violation messages.

**Feedback Agent**  
File: `tasks/pipeline_task.py`

Currently implemented as a placeholder:

```python
def feedback_agent(turtle_graph: str, violations: list[str]) -> dict[str, str]:
    return {"reasoning": "", "corrected_graph": turtle_graph}
```

The intended behavior is to pass validation errors and the current graph to an LLM repair agent, then store both the reasoning and corrected graph for each iteration.

## Data Model

SQLite is used for persistent job state.

Default database URL:

```env
DATABASE_URL=sqlite:////app/storage/jobs.db
```

Main tables:

- `jobs`: job id, status, input text, iteration counters, final graph, validation flag, webhook URL, timestamps.
- `iterations`: validation violations, repair reasoning, triple counts before/after, timestamp.

Job statuses:

- `Pending`
- `Extracting`
- `Building`
- `Validating`
- `Repairing`
- `Complete`
- `Error`
- `MaxIterationsReached`

## Ontology and Validation Assets

Ontology files:

- `ontology/family_orig.owl`: provided/source family ontology.
- `ontology/family_extended.ttl`: merged and extended ontology artifact used by the pipeline.
- `ontology/ontology_summary.md`: generated ontology summary.

SHACL file:

- `shapes/family_shapes.ttl`

Current SHACL constraints cover examples such as:

- `hasFather` must have at most one value and the referenced person must be male.
- `hasMother` must have at most one value and the referenced person must be female.
- Brother, sister, son, daughter, husband, and wife relations must point to the expected sex.
- `hasSex` must be `fhkb:Male` or `fhkb:Female`.
- Birth, death, and marriage years must be integer values in a plausible range.
- Death year must not be earlier than birth year.
- Marriage partners must match expected sex constraints.

## API Endpoints

Base URL when running locally:

```text
http://localhost:8000
```

### Health Check

```http
GET /health
```

Returns a lightweight service health response.

### Initiate Knowledge Graph Extraction

```http
POST /jobs
Content-Type: application/json
```

Request:

```json
{
  "text": "John Doe was born in 1900. He married Jane Smith in 1925. Their daughter Mary Doe was born in 1930.",
  "webhook_url": "https://example.com/webhook"
}
```

`webhook_url` is optional.

Response:

```json
{
  "job_id": "generated-uuid",
  "status": "Pending",
  "created_at": "2026-07-06T12:00:00Z"
}
```

### Status of Knowledge Graph Extraction

```http
GET /jobs/{job_id}/status
```

Response:

```json
{
  "job_id": "generated-uuid",
  "status": "Complete",
  "current_iteration": 1,
  "max_iterations": 10,
  "last_error": null,
  "created_at": "2026-07-06T12:00:00Z",
  "updated_at": "2026-07-06T12:00:05Z"
}
```

### Retrieve Validated Graph

```http
GET /jobs/{job_id}/graph?format=turtle
```

Supported formats:

- `turtle`
- `json_ld`
- `rdf_xml`

The endpoint returns `409 Conflict` until the job status is `Complete`.

### Retrieve Iteration Details

```http
GET /jobs/{job_id}/iterations
```

Returns stored validation/repair history:

```json
{
  "job_id": "generated-uuid",
  "iterations": [
    {
      "iteration_number": 1,
      "violations": [],
      "llm_reasoning": "",
      "triples_before": 18,
      "triples_after": 18,
      "timestamp": "2026-07-06T12:00:05Z"
    }
  ]
}
```

## Running with Docker

1. Create an environment file:

```bash
cp .env.example .env
```

2. Edit `.env` and set your OpenAI API key:

```env
OPENAI_API_KEY=your_key_here
```

3. Start the full stack:

```bash
docker compose up --build
```

Services:

- API: `http://localhost:8000`
- API docs: `http://localhost:8000/docs`
- Redis: internal service used by Celery
- Worker: Celery worker that runs the pipeline

4. Submit a job:

```bash
curl -X POST http://localhost:8000/jobs \
  -H "Content-Type: application/json" \
  -d '{
    "text": "John Doe was born in 1900. He married Jane Smith in 1925. Their daughter Mary Doe was born in 1930."
  }'
```

5. Check status:

```bash
curl http://localhost:8000/jobs/<job_id>/status
```

6. Retrieve the graph:

```bash
curl "http://localhost:8000/jobs/<job_id>/graph?format=turtle"
```

## Running Locally Without Docker

Docker is the recommended path because Redis, API, worker, and storage paths are already wired together.

For local development:

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create `.env`:

```bash
cp .env.example .env
```

4. For local non-Docker execution, adjust `.env`:

```env
REDIS_URL=redis://localhost:6379/0
DATABASE_URL=sqlite:///storage/jobs.db
OPENAI_API_KEY=your_key_here
```

5. Start Redis separately.

6. Start the API:

```bash
uvicorn api.main:app --reload
```

7. Start the worker in another terminal:

```bash
celery -A celery_app worker --loglevel=INFO --concurrency=4
```

## Configuration

| Variable | Default | Purpose |
| --- | --- | --- |
| `OPENAI_API_KEY` | required for real extraction | API key for the OpenAI client. |
| `OPENAI_MODEL` | `gpt-4o-mini` | Model used by the Extraction Agent. |
| `REDIS_URL` | `redis://redis:6379/0` | Celery broker and result backend. |
| `DATABASE_URL` | `sqlite:////app/storage/jobs.db` | SQLite database path in Docker. |
| `LOG_LEVEL` | `INFO` | Logging threshold. |
| `MAX_ITERATIONS` | `10` | Maximum validation/repair loop iterations. |
| `WEBHOOK_TIMEOUT_SECONDS` | `10` | Per-attempt webhook timeout. |
| `WEBHOOK_MAX_ATTEMPTS` | `3` in code | Maximum webhook delivery attempts. |

## Sample Input and Resulting Graph

Sample input:

```text
John Doe was born in 1900 and died in 1970. He was also known as Johnny.
John married Jane Doe in 1945. Jane Doe was born in 1925.
Jane's father was John Doe.
```

Representative structured extraction:

```json
{
  "entities": [
    {
      "id": "john_doe_1900",
      "label": "John Doe",
      "sex": "Male",
      "birth_year": 1900,
      "death_year": 1970,
      "aliases": ["Johnny"]
    },
    {
      "id": "jane_doe_1925",
      "label": "Jane Doe",
      "sex": "Female",
      "birth_year": 1925,
      "death_year": null,
      "aliases": []
    }
  ],
  "relations": [
    {
      "subject": "jane_doe_1925",
      "predicate": "hasFather",
      "object": "john_doe_1900"
    }
  ],
  "marriages": [
    {
      "male_partner": "john_doe_1900",
      "female_partner": "jane_doe_1925",
      "marriage_year": 1945
    }
  ]
}
```

Representative Turtle:

```turtle
@prefix fhkb: <http://www.example.com/genealogy.owl#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

fhkb:john_doe_1900
    a fhkb:Person, owl:NamedIndividual ;
    rdfs:label "John Doe" ;
    fhkb:alsoKnownAs "Johnny" ;
    fhkb:hasBirthYear 1900 ;
    fhkb:hasDeathYear 1970 ;
    fhkb:hasSex fhkb:Male .

fhkb:jane_doe_1925
    a fhkb:Person, owl:NamedIndividual ;
    rdfs:label "Jane Doe" ;
    fhkb:hasBirthYear 1925 ;
    fhkb:hasFather fhkb:john_doe_1900 ;
    fhkb:hasSex fhkb:Female .

fhkb:marriage_john_doe_1900_jane_doe_1925_1945
    a fhkb:Marriage, owl:NamedIndividual ;
    fhkb:hasFemalePartner fhkb:jane_doe_1925 ;
    fhkb:hasMalePartner fhkb:john_doe_1900 ;
    fhkb:hasMarriageYear 1945 .
```

## Testing

Run the test suite:

```bash
pytest
```

The current tests cover:

- OpenAI extraction agent schema handling, retries, and malformed responses.
- RDF generation from structured extraction output.
- Entity id sanitization and namespace safety.
- Extended ontology preservation and datatype property declarations.
- SHACL shape behavior using `pyshacl`.
- API route behavior and error responses.
- Max-iteration configuration.
- Webhook retry and delivery marking behavior.

## Design Decisions

### Custom Multi-Agent Pipeline

The implementation uses a small custom pipeline instead of a heavy agent framework. This keeps the control flow explicit:

1. extract,
2. build RDF,
3. validate,
4. repair,
5. repeat until success or termination.

This also makes API status transitions and iteration persistence easier to test.

### Asynchronous API

Extraction and validation may involve LLM calls and graph validation, so job creation returns immediately with a `job_id`. Celery runs the long workflow in the background, while clients poll status or receive a webhook.

### SQLite for Current Scope

SQLite is enough for a local internship prototype and keeps Docker setup simple. The storage layer is isolated in `storage/database.py`, so it can later be replaced by PostgreSQL or another durable database.

### Strict Extraction Schema

The Extraction Agent uses OpenAI structured output to reduce parsing ambiguity and keep the KG Builder deterministic. The KG Builder does not accept arbitrary predicates.

### Marriage as an Entity

Marriage is represented as a separate `fhkb:Marriage` individual rather than only a direct relation. This matches the ontology shape where marriage can have partners and a marriage year.

### SHACL Before OWL Reasoning

The repository currently leans toward SHACL because the task requires clear validation errors that a feedback agent can interpret. SHACL also makes cardinality, datatype, and relation-specific sex constraints explicit.

## Limitations

- The pipeline currently marks generated graphs as valid because the runtime `validation_agent` is a placeholder.
- The feedback loop records iterations but does not yet perform real graph repair.
- Extraction quality depends on the selected OpenAI model and prompt.
- There is no benchmark dataset or metric report yet.
- The API retrieves graphs only after `Complete`; failed graphs saved after max iterations are not exposed by the graph endpoint.
- SQLite is appropriate for the current prototype but not ideal for high-concurrency production workloads.
- Authentication, authorization, rate limiting, and request size limits are not implemented.

## Future Work

Highest priority:

- Replace `validation_agent` with real `pyshacl.validate` execution against `shapes/family_shapes.ttl`.
- Parse SHACL validation reports into concise violation messages for iteration history.
- Replace `feedback_agent` with an LLM repair agent that receives the current Turtle graph and validation errors.
- Add tests for full failing-then-repaired pipeline iterations.
- Add sample end-to-end runs after real validation is connected.

Evaluation/reporting:

- Create a small gold-standard family text dataset.
- Measure entity extraction precision/recall.
- Measure relation extraction precision/recall.
- Track validation error counts per iteration.
- Report whether iterative repair reduces errors and preserves correct triples.
- Document failure cases and prompt improvements.

API and operations:

- Add endpoint authentication.
- Add pagination or filtering for job history if job listing is introduced.
- Add request size limits and clearer API error messages.
- Add webhook signing.
- Consider PostgreSQL for multi-user or deployed environments.

Ontology improvements:

- Expand supported predicates if needed.
- Add inverse relation materialization or reasoning.
- Decide whether unknown-sex entities should remain untyped, be repaired by feedback, or be represented with a formal unknown value outside the current SHACL constraints.

## Project Structure

```text
.
├── agents/
│   ├── extraction_agent.py       # LLM extraction agent
│   └── kg_builder_agent.py       # RDF/Turtle builder
├── api/
│   ├── main.py                   # FastAPI app
│   ├── task_queue.py             # Celery dispatch helper
│   ├── models/job.py             # Pydantic request/response models
│   └── routers/
│       ├── health.py             # Health endpoint
│       └── jobs.py               # Job API endpoints
├── core/
│   └── logging_config.py         # structlog setup
├── ontology/
│   ├── family_orig.owl           # Source ontology
│   ├── family_extended.ttl       # Merged/extended ontology artifact
│   └── ontology_summary.md       # Ontology summary
├── shapes/
│   └── family_shapes.ttl         # SHACL validation shapes
├── storage/
│   └── database.py               # SQLite persistence
├── tasks/
│   └── pipeline_task.py          # Celery pipeline task and agent loop
├── tests/                        # Unit tests
├── utils/
│   └── rdf.py                    # RDF parsing/serialization helpers
├── celery_app.py                 # Celery configuration
├── docker-compose.yml            # API, worker, Redis stack
├── Dockerfile                    # Python service image
└── requirements.txt              # Python dependencies
```

