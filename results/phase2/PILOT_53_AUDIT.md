# Phase 2 pilot audit: examples 1–53

## Results

| Method | Answer rate | Exact match | Mean token F1 |
|---|---:|---:|---:|
| Direct text LLM | 96.23% | 64.15% | 77.05% |
| Symbolic SPARQL | 79.25% | 47.17% | 59.38% |

The symbolic system answered 42 examples and returned no result for 11. There were no remaining execution failures after retrying example 36.

## Symbolic error taxonomy

| Cause | Count | Example IDs |
|---|---:|---|
| Query planning or comparison | 10 | 7, 9, 12, 21, 25, 31, 33, 36, 47, 50 |
| Compatible answer rejected by surface form | 12 | 4, 5, 10, 11, 17, 24, 40, 41, 45, 48, 49, 51 |
| Missing or conflicting graph content | 6 | 14, 19, 30, 37, 38, 42 |

### Query-planning failures

- Some queries added unnecessary constraints, such as requiring both a composer and performer or requiring an occupation triple absent from the graph.
- Some used only `rdfs:label` when the question form was stored as `skos:altLabel`.
- Mixed `xsd:gYear` and `xsd:date` values were ordered incorrectly.
- Lifespan arithmetic cast complete dates directly to integers and selected the wrong person.
- One same-country query interpreted “Tomskoye, Amur Oblast” as two separate entities.
- One query added language tags not present on graph labels.

### Surface-form failures

Examples include `1975-08-08` versus `August 8, 1975`, `England` versus `English`, `Germany` versus `German`, `Parkinson's disease` versus `Parkinson`, and `New York, New York` versus `New York`. These should not all be converted into exact matches. Exact match and token F1 should remain, while explicitly justified date/demonym equivalence and a separate semantic-equivalence score can be added.

### Graph-content failures

The final graph lacks the required death place, mother, burial place, or spouse facts in examples 14, 19, 37, 38, and 42. Example 30 contains `Mexico, D.F.` as the director's birthplace while the reference answer is `France`. These cannot be fixed by changing SPARQL alone.

## Required work before 1,000 examples

1. Retry empty-result queries with execution feedback and constrained query relaxation.
2. Add tested date-ordering and lifespan-query instructions.
3. Add date-format and demonym equivalence to shared scoring.
4. Add an independently reported semantic-equivalence metric.
5. Record per-example failure categories so missing graph facts are not attributed to SPARQL execution.
