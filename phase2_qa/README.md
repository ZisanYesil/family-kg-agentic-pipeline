# Phase 2: Question Answering

This package evaluates answer generation separately from Phase 1 graph extraction.
Every primary comparison must use the identical frozen 1,000-example cohort.
Reports retain the benchmark-compatible correction rate as `exact_match` and add
`strict_exact_match`, which requires normalized answer equality and does not apply
containment, date-precision, Boolean-alias, or country-demonym compatibility rules.

## Experimental conditions

1. **Direct text baseline**: the LLM receives only the question and original text.
2. **Reasoned-graph symbolic QA**: relation-guided deterministic traversal and SPARQL-style
   graph retrieval over the final SHACL-plus-inference graph. The benchmark reads the
   question type and relation chain stored in `manifest.csv`.
3. **Question-only ablation**: an LLM generates complete SPARQL from the question,
   ontology vocabulary, and graph entity labels.

The primary symbolic benchmark is implemented by `run_relation_guided_symbolic_qa.py` and reuses
the deterministic relation resolver in `run_sparql_generic.py`. The answer and ground-truth
graph are not used for retrieval. The question-only generator remains available in
`run_symbolic_sparql_qa.py` as an ablation.

## Direct baseline

```bash
python -m phase2_qa.run_direct_text_qa \
  --dataset data/final_1000 --ids 1-1000 \
  --output results/phase2/direct_text.json
```

The runner is resumable and records the model, prompt version, latency, token usage, raw
answer, normalized exact match, and token-level F1 for every example.

## Primary symbolic system

```bash
python -m phase2_qa.run_relation_guided_symbolic_qa \
  --dataset data/final_1000 --ids 1-1000 --graph-stage reasoned \
  --output results/phase2/symbolic_relation_guided.json
```

The QA step over an already constructed graph makes no LLM calls and consumes no
LLM tokens. This accounting excludes upstream graph construction: extraction and
SHACL feedback may use LLM calls and must be reported separately.

## Repeatability verification

Verify that fixed graphs, ontology, manifest guidance, and questions produce the
same answers and retrieval traces across repeated symbolic executions:

```bash
python -m phase2_qa.verify_symbolic_repeatability \
  --dataset data/final_1000 --ids 1-1000 --graph-stage reasoned --runs 3 \
  --output results/phase2/symbolic_repeatability_1000.json
```

The verifier fingerprints every input file and each run's canonical answers and
retrieval traces. It exits unsuccessfully and records per-example mismatches if any
run differs. Its scope is the deterministic QA stage, not upstream LLM extraction
or repair.

## Paired comparison

```bash
python -m phase2_qa.compare_qa \
  --baseline results/phase2/direct_text.json \
  --system results/phase2/symbolic_relation_guided.json \
  --output results/phase2/comparison.json
```

## Question-only ablation

```bash
python -m phase2_qa.run_symbolic_sparql_qa \
  --dataset data/final_1000 --ids 1-1000 \
  --output results/phase2/question_only_sparql.json
```
