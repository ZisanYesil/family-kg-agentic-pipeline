# Ontology-Driven Knowledge Graph Construction Pipeline

This repository implements a hybrid neuro-symbolic pipeline that transforms unstructured text into ontology-grounded RDF knowledge graphs, checks and selectively repairs them with SHACL, materializes ontology-supported consequences, and queries the resulting graphs deterministically.

The project studies why structured output remains useful even when a large language model (LLM) can answer a question directly from text. A direct answer is generated for one request; the graph is a persistent, machine-checkable representation that can be validated, reasoned over, inspected, reused, and queried repeatedly.

The implementation is evaluated in two separate phases:

1. **Graph construction and symbolic enhancement:** assess extracted factual relations before and after constrained SHACL-guided processing and ontology-based inference.
2. **Downstream question answering:** compare direct LLM answers from the original question and context with deterministic querying of the completed graph.

These phases use different units of evaluation. Triple-level precision, recall, and F1 describe graph construction; answer-level exact match and token F1 describe question answering.


## Ontology-driven configuration

The schema-facing implementation is ontology-driven rather than hard-coded to a fixed list of classes and properties. At runtime, it parses a supplied OWL/Turtle ontology and uses the discovered vocabulary and structural axioms to configure extraction, relation mapping, RDF construction, validation, and inference.

The ontology used for the reported experiment is task-minimal and contains:

- 14 classes;
- 42 object properties;
- 5 datatype properties;
- 17 subproperty axioms;
- 10 inverse-property axioms; and
- 2 symmetric properties.

Thirty-six object properties are exposed to extraction after excluding an abstract superproperty and redundant inverse-facing choices. The ontology includes shallow class organization, such as `Agent`, `Artifact`, and `Place`, together with richer property relationships relevant to the benchmark.

A different compatible ontology can reconfigure the core schema-facing stages without rewriting their vocabulary-handling logic. This is not a claim of universal zero-configuration portability: an ontology must contain usable declarations and sufficiently informative metadata, and constraints that cannot be derived from structural axioms may require supplementary SHACL shapes. The current empirical evaluation uses one task-specific ontology.

The evaluated ontology is located at [`ontology/ontology.ttl`](ontology/ontology.ttl).

## Knowledge-graph construction

### 1. Ontology-aware information extraction

The extraction stage receives only the natural-language question and its original context. It does **not** receive the reference answer, reference graph, benchmark question type, or expected relation sequence.

The supplied ontology dynamically configures the structured extraction schema and prompt. The evaluated extraction model is `gpt-oss:120b`, and its output is parsed as strict structured JSON containing entities, attributes, aliases, and candidate relations.

### 2. Relation mapping and RDF construction

Candidate relations are first mapped deterministically to ontology properties. An LLM fallback is used only for unresolved candidates, and returning no mapping is permitted when the evidence does not justify one. Domain and range information is used to check property orientation.

The RDF construction stage creates:

- ontology class assertions;
- human-readable labels and aliases;
- datatype-property assertions; and
- ontology-grounded object-property assertions.

Construction-time entity resolution does not use benchmark answers or reference RDF. Entities are merged only under guarded conditions, including a unique shared Wikidata identifier, compatible types, and no conflicting evidence.

### 3. SHACL validation and constrained feedback

Structural SHACL shapes are generated from the loaded ontology. The validator also records diagnostics such as unmapped extracted phrases. Findings receive stable fingerprints so that repeated iterations can be tracked consistently.

The feedback stage can propose a small set of graph edits, including adding or removing a relation or replacing a literal. A proposal is applied only after deterministic checks confirm that it is supported by:

- the source text;
- the supplied ontology;
- the current graph state; and
- the reported validation finding.

Accepted edits are applied atomically. A run may stop with unresolved findings rather than forcing the graph to conform. The experiment permits at most three repair iterations.

Across the frozen 1,000-example cohort:

| SHACL-processing outcome | Examples |
|---|---:|
| No feedback required | 947 |
| At least one accepted repair | 20 |
| Unresolved after processing | 33 |
| Pipeline failure | 0 |

These categories describe pipeline outcomes; they do not imply that every accepted graph statement is factually correct.

### 4. Ontology-based inference

The pipeline uses HermiT through Owlready2 together with explicit closure rules for the ontology constructs required by the experiment. These include:

- subclass and type propagation;
- domain and range typing;
- subproperty and equivalent-property propagation;
- inverse properties; and
- symmetric properties.

The pipeline does not infer that a parent relation is transitive. In total, 4,537 ontology-supported statements were materialized over the evaluation cohort.

## Evaluation data

The experiment uses a frozen cohort derived from the development split of **2WikiMultiHopQA**. Candidate selection was performed before observing evaluation scores: 1,000 primary examples and a 300-example reserve were sampled using a rare-relation-first procedure with seed 42, audited, and then frozen.

| Cohort characteristic | Value |
|---|---:|
| Evaluation examples | 1,000 |
| Compositional questions | 486 |
| Comparison questions | 350 |
| Inference questions | 96 |
| Bridge-comparison questions | 68 |
| Mean context length | 642.93 words |
| Mean reference graph size | 2.36 triples |
| Mean original extracted graph size | 11.87 triples |

The frozen manifests and per-example artifacts are under [`data/final_1000`](data/final_1000).

## Phase 1: graph-level evaluation

The original extracted graph and the final graph produced after constrained SHACL processing and ontology-based inference are evaluated under strict triple matching. The reference graph is used in its asserted form for the original condition and is closed under the same ontology for the final condition, so an entailed statement is not counted on only one side of the final comparison.

Entity alignment is used only for evaluation and is frozen from the original graph condition before being applied unchanged to the final graph condition. It combines lexical, alias, and contextual similarity using `paraphrase-multilingual-MiniLM-L12-v2`, a threshold of 0.55, and an ambiguity margin of 0.05. The reference answer and reference RDF are never used during graph construction or graph-based retrieval.

After accepted entity identifiers are substituted, scoring uses exact equality of canonicalized RDF subjects, predicates, and objects. Plain literals and `xsd:string` literals share a representation. For four date predicates, a year and a complete date may match at year precision when at least one graph explicitly uses `xsd:gYear`; two complete dates must match exactly. The evaluator does not collapse related ontology predicates: for example, `hasFather` and `hasParent` match only when the corresponding ontological consequence is present in the evaluated graph.

| Condition | TP | FP | FN | Micro precision | Micro recall | Micro F1 | Macro precision | Macro F1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Original graphs | 1,859 | 10,014 | 498 | 15.66% | 78.87% | 26.13% | 16.53% | 26.82% |
| Final graphs | 8,260 | 1,542 | 983 | 84.27% | 89.36% | 86.74% | 84.80% | 86.89% |

From the original to the final graph condition, micro precision increased by 68.61 percentage points, recall by 10.49 points, and F1 by 60.61 points. At example level, F1 increased for 993 graphs, was unchanged for seven, and decreased for none. Because the final condition includes both constrained feedback and ontology closure, this comparison measures the complete graph-transformation process rather than attributing the change to either component alone.

## Phase 2: question answering

### Conditions

**Direct-text LLM QA** receives exactly two inputs: the original question and the original context text. No ontology, graph, reference answer, question type, or relation sequence is supplied.

**Deterministic graph QA** receives the completed reasoned graph and frozen benchmark guidance specifying the question category and relation sequence. It does not receive the reference answer or reference graph. The guidance removes natural-language query interpretation from the measured retrieval condition, so the result evaluates deterministic traversal of the available structured knowledge rather than a complete open-ended natural-language graph interface.

### Results

| QA condition | Strict exact match | Compatible exact match | Token F1 | Answer rate |
|---|---:|---:|---:|---:|
| Direct LLM over question + text | 66.40% | 86.20% | 87.13% | 95.00% |
| Deterministic QA over reasoned graph | 63.10% | 79.50% | 80.40% | 88.70% |

The direct LLM baseline is stronger on answer accuracy. The structured condition is therefore not presented as a universal replacement for direct answering. Its additional value is that the graph persists after construction and supports machine-checkable processing, inference, inspectable retrieval traces, repeated querying, and deterministic execution over fixed inputs.

The paired compatible-exact-match outcomes are:

| Outcome | Examples |
|---|---:|
| Both systems correct | 766 |
| Direct LLM only correct | 96 |
| Graph QA only correct | 29 |
| Neither correct | 109 |

### LLM usage and repeatability

The direct baseline made 1,000 LLM calls. Token telemetry was available for 982 responses:

| Direct-QA token telemetry | Tokens |
|---|---:|
| Prompt | 1,090,556 |
| Completion | 155,443 |
| Total | 1,245,999 |

The 18 responses without telemetry are not estimated, so these totals are lower bounds for the complete direct-QA run.

The evaluated graph-query stage made zero LLM calls and consumed zero generation tokens after graph construction. This does not mean the full graph workflow is free of LLM cost: extraction and some feedback operations occur at construction time. A fair amortized cost comparison across multiple questions requires separate construction-token measurements and is future work.

Repeatability was tested by running graph QA three times over all 1,000 frozen examples. Answers and retrieval traces were identical across all runs. This establishes repeatability for the fixed graphs, manifests, software, and execution environment used in the experiment; it does not imply that upstream LLM-based graph construction is itself deterministic.

## Running the pipeline

### Requirements

- Python 3.10 or newer
- Java for HermiT reasoning
- Access to an OpenAI-compatible chat-completions endpoint

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

Configure the model endpoint. Use environment variables or a local `.env` file; never commit credentials.

```bash
export LLM_API_KEY="your-api-key"
export LLM_BASE_URL="https://your-endpoint.example/v1"
export LLM_MODEL="gpt-oss:120b"
```

The exact variable names accepted by individual entry points are documented in their `--help` output and configuration modules.

### Reproduce the frozen data workflow

Build the candidate pool:

```bash
python build_dataset.py \
  --input data/dev.parquet \
  --out data/candidates_1300 \
  --n 1000 \
  --reserve 300 \
  --seed 42
```

Run ontology-grounded graph construction:

```bash
python run_agent_pipeline.py data/candidates_1300 \
  --ids 1-1300 \
  --output-dir data/candidate_pipeline \
  --ontology ontology/ontology.ttl \
  --shacl-repair \
  --max-repair-iterations 3
```

Freeze the 1,000-example evaluation cohort:

```bash
python finalize_dataset.py \
  --candidate-dir data/candidates_1300 \
  --pipeline-dir data/candidate_pipeline \
  --output-dir data/final_1000 \
  --target 1000
```

Run SHACL processing, inference, and evaluation-only alignment:

```bash
python run_shacl_pipeline.py \
  --input-dir data/final_1000 \
  --ids 1-1000 \
  --max-repair-iterations 3 \
  --summary-output data/final_1000/shacl_summary.json

python run_inference_pipeline.py \
  --input-dir data/final_1000 \
  --output-dir data/final_1000 \
  --ids 1-1000 \
  --ontology ontology/ontology.ttl \
  --summary-output data/final_1000/inference_summary.json

python run_evaluation_alignment.py \
  --input-dir data/final_1000 \
  --ids 1-1000 \
  --ontology ontology/ontology.ttl \
  --summary-output data/final_1000/alignment_summary.json
```

### Run Phase 2 QA

Phase 2 entry points should be invoked as modules from the repository root:

```bash
python -m phase2_qa.run_direct_text_qa \
  --input-dir data/final_1000 \
  --ids 1-1000

python -m phase2_qa.run_relation_guided_symbolic_qa \
  --input-dir data/final_1000 \
  --ids 1-1000 \
  --graph-stage reasoned

python -m phase2_qa.compare_qa \
  --input-dir data/final_1000 \
  --ids 1-1000

python -m phase2_qa.verify_symbolic_repeatability \
  --input-dir data/final_1000 \
  --ids 1-1000 \
  --graph-stage reasoned \
  --runs 3
```

Use `--help` on each command for output paths and optional settings.

## Asynchronous API

The repository also exposes an asynchronous FastAPI service for individual graph-construction jobs.

Start it locally:

```bash
uvicorn api.app:app --host 0.0.0.0 --port 8000
```

Submit a job:

```bash
curl -X POST http://localhost:8000/jobs \
  -H 'Content-Type: application/json' \
  -d '{
    "text": "The film had musical score by Rajesh Khanna. He was married to Dimple Kapadia.",
    "question": "Who is the spouse of the composer of the film?",
    "ontology_path": "ontology/ontology.ttl"
  }'
```

Main endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/health` | Service health |
| `POST` | `/jobs` | Create a graph-construction job |
| `GET` | `/jobs/{job_id}` | Job status and summary |
| `GET` | `/jobs/{job_id}/graph` | Final graph artifact |
| `GET` | `/jobs/{job_id}/iterations` | Validation and repair history |

An optional webhook URL may be included when submitting a job. See the API models and generated OpenAPI documentation at `/docs` for the authoritative request and response schemas.

Run with Docker Compose:

```bash
docker compose up --build
```

## Artifact layout

Each processed example retains intermediate artifacts so that construction decisions can be inspected rather than reduced to a final answer. Depending on the invoked workflow, these include:

- the frozen input manifest;
- raw structured extraction;
- original RDF graph;
- mapping diagnostics;
- SHACL reports and feedback iterations;
- accepted and rejected repair records;
- inferred statements and the reasoned graph;
- frozen evaluation alignment;
- QA answer and retrieval trace; and
- token/call telemetry when exposed by the model endpoint.

Generated reports and manuscript materials are intentionally excluded from version control. The repository `.gitignore` covers the local `article/`, `output/pdf/`, and `tmp/pdfs/` paths so that draft text, figures, and regenerated reports are not published accidentally.

## Repository structure

```text
api/                         FastAPI application and job models
agents/                      Extraction, mapping, feedback, and orchestration logic
ontology/                    Task-minimal OWL/Turtle ontology
shacl/                       Shape generation, validation, and repair support
inference/                   Ontology loading and materialized closure
entity_resolution/           Guarded construction-time entity resolution
evaluation_alignment/        Frozen, evaluation-only entity alignment
phase2_qa/                   Direct-text QA, graph QA, comparison, repeatability
data/                        Source, candidate, frozen, and per-example artifacts
tests/                       Unit and integration tests
run_agent_pipeline.py        Batch graph-construction entry point
run_shacl_pipeline.py        SHACL processing entry point
run_inference_pipeline.py    Inference entry point
run_evaluation_alignment.py  Alignment entry point
build_dataset.py             Candidate-cohort construction
finalize_dataset.py          Frozen-cohort finalization
```

## Tests

Run the test suite from the repository root:

```bash
pytest -q
```

For changes to evaluation logic, also regenerate a small fixed subset and inspect its original graph, final graph, alignment, and QA trace. Metric code should be tested with explicit cases containing metadata predicates to ensure that only factual relations enter Phase 1 scoring.

## Limitations

- The reported study uses one dataset, one task-specific ontology, and one principal extraction model.
- Cross-domain portability of the ontology-driven implementation has not yet been evaluated end to end.
- SHACL conformance verifies conformance to supplied shapes, not factual truth or graph completeness.
- Inference can materialize only consequences licensed by the ontology and available assertions; it cannot recover every fact omitted during extraction.
- Some repair decisions use an LLM, although every accepted edit passes deterministic support checks.
- Graph QA uses frozen relation guidance and therefore does not measure unrestricted natural-language query interpretation.
- Zero query-time LLM use applies after graph construction and should not be confused with zero total pipeline cost.
- Repeatability was established for fixed graph inputs, not for stochastic upstream construction.

## Data and licensing

2WikiMultiHopQA remains subject to its original dataset terms. Model access is subject to the provider's terms and deployment policy. Add an explicit repository license before redistributing this software if one is not already present.
