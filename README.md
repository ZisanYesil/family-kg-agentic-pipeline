# Family KG Agentic Pipeline

Family KG Agentic Pipeline is an agentic AI system for converting unstructured family narratives into ontology-grounded knowledge graphs. The project focuses on extracting people, attributes, and family relationships from text; representing them as RDF according to a Family Ontology; validating the generated graph with semantic constraints; and improving the result through an automated feedback loop.

The system is designed for the internship task: **Agentic AI for Family-Ontology Knowledge Graph Construction and Iterative Improvement**.

## Project Goal

The goal is to build a reproducible pipeline that can:

- read narrative or semi-structured family-history text,
- identify individuals and family-related attributes,
- extract relationships such as parent, sibling, spouse, son, and daughter,
- generate an RDF knowledge graph aligned with a Family Ontology,
- validate the graph using OWL reasoning or SHACL constraints,
- interpret validation errors and iteratively improve the graph,
- expose the workflow through an asynchronous API.

In short, the project turns natural-language family descriptions into machine-readable, ontology-consistent knowledge graphs.

## System Overview

The pipeline follows a multi-agent architecture. Each agent has a focused responsibility, and the agents communicate automatically until the graph passes validation or a maximum iteration limit is reached.

```text
Input text
   |
   v
Extraction Agent
   |
   v
KG Builder Agent
   |
   v
Validation Agent
   |
   v
Feedback Agent
   |
   +---- if errors exist, revise and repeat
   |
   v
Validated RDF knowledge graph
```

## Agent Roles

### Extraction Agent

The Extraction Agent analyzes the input text and identifies:

- people mentioned in the narrative,
- attributes such as name, gender, birth year, death year, and aliases,
- family relationships between people,
- marriage information when available.

Its output is a structured intermediate representation that can be converted into RDF.

### KG Builder Agent

The KG Builder Agent converts the extracted structure into RDF triples. It aligns people, relationships, and attributes with the Family Ontology by using ontology-defined classes, object properties, and data properties.

The generated graph may be serialized as formats such as Turtle, JSON-LD, or RDF/XML.

### Validation Agent

The Validation Agent checks whether the generated knowledge graph is consistent with the ontology and validation rules. It is responsible for detecting issues such as:

- invalid domain or range usage,
- inconsistent relationship semantics,
- cardinality violations,
- missing or malformed attribute values,
- logical inconsistencies in family relationships.

Validation can be performed with OWL reasoners or SHACL shapes.

### Feedback Agent

The Feedback Agent reads structured validation errors and asks the configured LLM for a strict `FeedbackPlan`. The model cannot replace the graph directly: every proposed add, remove, or literal replacement is checked against the ontology, current graph, source text, and targeted validation fingerprint before being applied atomically.

Unsafe plans fail the job without mutating the graph. Findings that cannot be repaired safely remain explicitly unresolved. The loop continues until the graph passes validation, repeats the same report, or reaches the configured iteration threshold.

## Knowledge Graph Construction

The knowledge graph is grounded in the Family Ontology. Extracted family data is represented with:

- individuals as ontology instances,
- family relationships as object-property triples,
- attributes such as birth year or gender as data-property triples,
- consistent IRIs for people and generated resources,
- ontology-aware relationship semantics.

Example input:

```text
John Smith was born in 1950. He married Mary Johnson in 1975.
Their daughter Anna Smith was born in 1980.
```

Example graph content, simplified:

```turtle
@prefix fhkb: <http://www.example.com/genealogy.owl#> .
@prefix ex: <http://example.org/family/> .

ex:john_smith a fhkb:Person ;
    fhkb:hasBirthYear 1950 ;
    fhkb:hasWife ex:mary_johnson ;
    fhkb:hasDaughter ex:anna_smith .

ex:mary_johnson a fhkb:Person ;
    fhkb:hasHusband ex:john_smith ;
    fhkb:hasDaughter ex:anna_smith .

ex:anna_smith a fhkb:Person ;
    fhkb:hasFather ex:john_smith ;
    fhkb:hasMother ex:mary_johnson ;
    fhkb:hasBirthYear 1980 .
```

## API

The API exposes the core workflow asynchronously. A user submits text, receives a job id immediately, and can then monitor the pipeline or retrieve the resulting graph.

Base URL when running locally:

```text
http://localhost:8000
```

### Health Check

```http
GET /health
```

### Start Knowledge Graph Extraction

```http
POST /jobs
Content-Type: application/json
```

Request:

```json
{
  "text": "John Smith was born in 1950. He married Mary Johnson in 1975. Their daughter Anna Smith was born in 1980.",
  "webhook_url": "https://example.com/webhook"
}
```

`webhook_url` is optional.

Response:

```json
{
  "job_id": "generated-job-id",
  "status": "Pending",
  "created_at": "2026-07-07T12:00:00Z"
}
```

### Check Job Status

```http
GET /jobs/{job_id}/status
```

The response includes the current status, current iteration, maximum iteration count, and the latest error if one exists.

Common statuses include:

- `Pending`
- `Extracting`
- `Building`
- `Validating`
- `Repairing`
- `Complete`
- `Error`
- `MaxIterationsReached`

### Retrieve Graph

```http
GET /jobs/{job_id}/graph?format=turtle
```

Supported output formats:

- `turtle`
- `json_ld`
- `rdf_xml`

### Retrieve Iteration Details

```http
GET /jobs/{job_id}/iterations
```

This endpoint returns the history of the iterative improvement process, including validation violations, feedback reasoning, and graph-size changes across iterations.

## Running the Application

### 1. Configure Environment Variables

Create a `.env` file based on `.env.example`.

```env
OPENAI_API_KEY=your_llm_provider_api_key_here
OPENAI_MODEL=gpt-4o-mini
REDIS_URL=redis://redis:6379/0
DATABASE_URL=sqlite:////app/storage/jobs.db
LOG_LEVEL=INFO
MAX_ITERATIONS=10
WEBHOOK_TIMEOUT_SECONDS=10
WEBHOOK_MAX_ATTEMPTS=3
DEFAULT_ONTOLOGY_PATH=ontology/family_extended.ttl
```

SQLite schema upgrades run automatically at API startup. Existing job and iteration
history is preserved; older databases receive the ontology path and repair-audit columns
required by the current pipeline.

### 2. Start with Docker Compose

```bash
docker compose up --build
```

This starts:

- the FastAPI service,
- the asynchronous worker,
- Redis for task queueing,
- persistent local storage for job data.

After startup, the API is available at:

```text
http://localhost:8000
```

Interactive API documentation is available at:

```text
http://localhost:8000/docs
```

## Local Development

Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

## Project Structure

```text
agents/       Agent logic for extraction and knowledge graph construction
api/          FastAPI application, request models, and routes
core/         Shared configuration and logging setup
ontology/     Family ontology files and ontology-related utilities
shapes/       SHACL validation shapes
storage/      Persistent job and iteration storage
tasks/        Asynchronous pipeline orchestration
tests/        Automated tests
```

## Deliverables Covered by the Project

The project is organized around the required internship deliverables:

- source code for the agentic workflow,
- ontology-integrated RDF generation,
- validation assets for ontology conformance,
- API endpoints for job creation, status tracking, graph retrieval, and iteration history,
- Dockerized execution,
- logging for pipeline observability,
- sample input and RDF-style output examples,
- documentation for running and using the application.

## Evaluation Focus

The system should be evaluated according to:

- correctness and completeness of extracted family relationships,
- conformance of generated RDF to the Family Ontology,
- ability to detect validation errors,
- ability to improve graph quality through feedback iterations,
- robustness of the automated multi-agent workflow,
- clarity and reproducibility of the API and documentation.

## Webhook Support

The job creation request can optionally include a webhook URL. When provided, the system can notify an external service after the asynchronous workflow finishes, allowing other applications to react to completed knowledge graph extraction jobs.
