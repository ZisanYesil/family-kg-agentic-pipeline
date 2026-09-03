# Phase 2 Question-Answering Evaluation Report

## Evaluation scope

The final evaluation uses all 1,000 examples in the frozen `data/final_1000`
cohort. No example was removed on the basis of either system's answer or score.
Both conditions were evaluated against the same reference answer for each ID.

The direct-text condition supplied the original question and unstructured text to
`gpt-oss:120b` using prompt contract `direct_text_qa_v1`. The symbolic condition
used the final reasoned extracted graph and deterministic relation-guided retrieval.
Its query construction was supplied with the question type and relation chain stored
in `manifest.csv`; it did not use the reference answer or ground-truth RDF graph for
answer retrieval.

## Metrics

- **Strict exact match** requires equality after the common normalization of case,
  punctuation, accents, whitespace, and English articles. It does not accept partial
  containment, date-precision compatibility, Boolean aliases, or country–demonym pairs.
- **Compatible correction rate** additionally accepts the benchmark's documented
  compatibility rules, including specific/short label containment, equivalent date
  representations, Boolean aliases, and predefined country–demonym pairs. This metric is
  stored under `exact_match` in the machine-readable result artifacts for compatibility
  with the benchmark implementation.
- **Token F1** measures token overlap and assigns full credit when the compatibility
  criterion considers the answers equivalent.
- **Answer rate** is the proportion of examples for which a nonempty answer was returned.
  Unanswered examples remain in every denominator and receive zero correctness and zero F1.

## Overall results

| Metric | Direct LLM | Symbolic system | Direct minus symbolic |
|---|---:|---:|---:|
| Strict exact match | 66.40% | 63.10% | +3.30 pp |
| Compatible correction rate | 86.20% | 79.50% | +6.70 pp |
| Mean token F1 | 87.13% | 80.40% | +6.73 pp |
| Answer rate | 95.00% | 88.70% | +6.30 pp |
| Answered examples | 950 | 887 | +63 |
| Unanswered examples | 50 | 113 | -63 |
| Execution failures | 0 | 0 | 0 |

All 1,000 direct API requests and all 1,000 symbolic executions are retained. Eighteen
direct responses contained no answer content. They are recorded as completed but
unanswered, rather than excluded or selectively rerun. They form part of the 50 direct
unanswered cases and receive zero on every correctness metric.

## Paired outcomes

The paired outcomes below use compatible correction on the same 1,000 IDs.

| Outcome | Examples | Percentage |
|---|---:|---:|
| Both systems correct | 766 | 76.60% |
| Direct LLM only correct | 96 | 9.60% |
| Symbolic system only correct | 29 | 2.90% |
| Neither system correct | 109 | 10.90% |

## Results by question type

### Direct LLM

| Question type | N | Answer rate | Strict exact | Compatible correction | Mean token F1 |
|---|---:|---:|---:|---:|---:|
| Bridge comparison | 68 | 94.12% | 89.71% | 89.71% | 89.71% |
| Comparison | 350 | 98.29% | 94.86% | 94.86% | 95.05% |
| Compositional | 486 | 91.98% | 40.95% | 79.63% | 80.34% |
| Inference | 96 | 98.96% | 75.00% | 85.42% | 90.88% |

### Symbolic system

| Question type | N | Answer rate | Strict exact | Compatible correction | Mean token F1 |
|---|---:|---:|---:|---:|---:|
| Bridge comparison | 68 | 91.18% | 88.24% | 88.24% | 88.24% |
| Comparison | 350 | 93.71% | 89.71% | 90.57% | 91.03% |
| Compositional | 486 | 85.60% | 40.12% | 71.60% | 72.21% |
| Inference | 96 | 84.38% | 64.58% | 72.92% | 77.52% |

The direct condition leads overall and in every question-type aggregate. The symbolic
condition nevertheless executes deterministically over reusable RDF graphs and produces
answers through explicit graph paths. Accuracy, answer coverage, provenance, inference
dependency, SHACL-repair dependency, and repeatability should therefore be reported as
separate dimensions rather than treating answer accuracy as the sole measure of system
quality.

## Reproducibility artifacts

- `results/phase2/direct_text_1000.json`: all direct predictions, scores, and execution metadata.
- `results/phase2/symbolic_relation_guided_1000.json`: all symbolic predictions, relation guidance, graph stage, and scores.
- `results/phase2/comparison_relation_guided_1000.json`: paired per-example outcomes and aggregate comparison.
- `data/final_1000/manifest.csv`: frozen cohort metadata, question types, and symbolic relation guidance.

The report values were computed from these artifacts. The evaluation implementation is
covered by the project test suite; 178 tests passed at the time this report was produced.
