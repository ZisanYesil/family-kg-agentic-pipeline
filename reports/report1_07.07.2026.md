# Weekly Report 1 - 07.07.2026

## Project

**Family KG Agentic Pipeline**  
Agentic AI for Family-Ontology Knowledge Graph Construction and Iterative Improvement

## Summary

During the first two week, I started the project by preparing the ontology resources, setting up the backend system architecture, and implementing the first two main agents of the pipeline: the Extraction Agent and the KG Builder Agent. The current system can accept unstructured family-related text through an API, process it asynchronously, extract structured family information using an LLM, and convert the extracted data into RDF/Turtle aligned with the Family Ontology.

## 1. Family Ontology Preparation

The first step was to obtain and inspect the provided Family Ontology. I added the original ontology file to the project and created an extended ontology artifact to support the knowledge graph construction process.

The ontology work focused on understanding the available classes, object properties, and data properties needed to represent family information. The main concepts used in the pipeline include people, gender information, birth and death years, family relations, and marriage records.

The ontology resources are organized under the `ontology/` directory.

## 2. System and Backend Setup

I set up the main application architecture around an asynchronous agentic pipeline. The system is designed so that users can submit a text input and receive a job id immediately while the actual extraction and graph construction process runs in the background.

The backend system includes:

- **FastAPI** for exposing REST API endpoints.
- **Celery** for running the long-running pipeline asynchronously.
- **Redis** as the Celery message broker and result backend.
- **SQLite** for storing job status, generated graphs, iteration details, and webhook delivery information.
- **Docker and Docker Compose** for running the API, worker, and Redis services together.
- **Structured logging** with `structlog` for tracking pipeline events and errors.

The API currently supports the main workflow required by the task:

- creating a knowledge graph extraction job,
- checking job status,
- retrieving the generated graph,
- retrieving iteration details.

I also added job lifecycle statuses such as `Pending`, `Extracting`, `Building`, `Validating`, `Repairing`, `Complete`, `Error`, and `MaxIterationsReached`.

## 3. Extraction Agent Implementation

I implemented the Extraction Agent, which is responsible for reading unstructured family narratives and converting them into a structured representation.

This agent uses the OpenAI Chat Completions API with the **Structured Outputs** feature. Instead of asking the model to return free-form text, I defined a strict JSON schema that the model must follow.
The structured output contains three main sections:

- `entities`: people mentioned in the text, with fields such as id, label, sex, birth year, death year, and aliases.
- `relations`: direct family relationships between people.
- `marriages`: marriage events represented separately from direct person-to-person relations.

The supported relationship vocabulary is intentionally restricted to ontology-compatible predicates:

- `hasFather`
- `hasMother`
- `hasBrother`
- `hasSister`
- `hasSon`
- `hasDaughter`
- `hasHusband`
- `hasWife`

The Extraction Agent also includes input validation, retry handling for OpenAI API connection errors, timeouts, and rate limits, and logging for successful and failed extraction attempts.

## 4. KG Builder Agent Implementation


The agent uses `rdflib` to generate RDF triples and serializes the final graph as Turtle. It binds the main prefixes used by the graph, including the Family Ontology namespace, RDF, RDFS, OWL, and XSD.

For each extracted person, the KG Builder Agent creates an ontology individual and adds available attributes such as:

- `rdfs:label` for the person's readable name,
- `fhkb:hasSex` for gender information,
- `fhkb:hasBirthYear` for birth year,
- `fhkb:hasDeathYear` for death year,
- `fhkb:alsoKnownAs` for aliases.

For family relationships, the agent converts each extracted relation into an object-property triple using the ontology predicate selected by the Extraction Agent. It also validates that unsupported predicates are not accepted.

Marriage information is modeled as a separate `fhkb:Marriage` individual. This allows the graph to represent both partners and the marriage year with dedicated properties:

- `fhkb:hasMalePartner`
- `fhkb:hasFemalePartner`
- `fhkb:hasMarriageYear`

I also added safeguards to the KG Builder Agent:

- entity ids are sanitized into stable URI local names,
- unsupported relation predicates raise an error,
- conflicting birth or death year values for the same entity are rejected,
- missing relation or marriage references are logged as diagnostics.


## 5. Pipeline Orchestration

I connected the implemented agents inside a Celery pipeline task. The current pipeline flow is:

1. The API creates a job and stores it in SQLite.
2. Celery starts the background pipeline.
3. The Extraction Agent extracts structured family information.
4. The KG Builder Agent converts the extracted information into RDF/Turtle.
5. The graph enters the validation and feedback loop structure.
6. The final graph and iteration details are stored for later retrieval.

The validation and feedback stages are already represented in the pipeline structure so that SHACL/OWL validation and LLM-based correction can be integrated into the next development phase.

## Current Outcome

By the end of the first two week, the project has a working foundation for the agentic knowledge graph pipeline. The main backend components are in place, the API can create and track jobs, the Extraction Agent can produce structured family data using OpenAI Structured Outputs, and the KG Builder Agent can generate ontology-aligned RDF/Turtle graphs from that data.
