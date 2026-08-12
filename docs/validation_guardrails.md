## Core Architecture

- Use a hybrid validation approach:
  - Dynamic SHACL for structural checks derived from `OntologySchema`.
  - OWL reasoning with `owlready2` + bundled HermiT for semantic/logical checks.
- Keep validation ontology-agnostic. Do not hardcode family-specific rules such
  as "father must be male" into SHACL; those belong to OWL reasoning when they
  come from equivalent classes, disjointness, restrictions, or property axioms.
- Run cheap SHACL checks before expensive reasoner checks. Reasoner execution can
  start after SHACL passes unless a later design explicitly supports safe merged
  execution.
- HermiT requires Java in Docker. The image must include
  `default-jre-headless`; do not remove the JRE layer while reasoner support is
  planned.

### Hand-Written Shape Supplements (e.g. `family_shapes.ttl`)

Hand-written shape files like `shapes/family_shapes.ttl` are optional supplements
to the dynamically generated SHACL graph, not part of the ontology-agnostic core.
They exist to cover checks the dynamic generator cannot express generically — see
`family_shapes.ttl`'s own rationale: it validates sex constraints via `hasSex`
instead of `sh:class fhkb:Man`/`fhkb:Woman`, because generated individuals are
typed `Person`, not `Man`/`Woman`.

- Merge a hand-written shapes file into the SHACL graph **only when the job's
  ontology namespace has a matching entry** in an explicit registry (e.g.
  `validation/shacl_runner.py::HAND_WRITTEN_SHAPES_BY_NAMESPACE`), not
  unconditionally for every job.
- Do not derive the hand-written shapes filename by guessing from the ontology
  filename; keep the namespace -> path mapping explicit so it is obvious which
  ontologies have a supplement and which don't.
- Unmatched namespaces (e.g. a mixed-domain test ontology) run with dynamic SHACL
  only. Log this at debug/info level, not as a warning, it is the expected
  default, not a missing feature.
- This keeps the dynamic SHACL generator itself fully ontology-agnostic: it never
  knows `family_shapes.ttl` exists. The registry lookup lives only in the
  runner/merge step.

## Structural Validation Scope

Dynamic SHACL should cover schema-derived checks:

- Domain violations.
- Range violations.
- Datatype violations.
- Cardinality violations from `owl:FunctionalProperty` via `sh:maxCount 1`.
- Later: inverse-functional or min-cardinality only when the schema loader
  explicitly extracts those ontology facts.
- Diagnostics from previous stages, especially dangling references and unmapped
  relations, should become validation-style violations instead of only logs.

The schema loader already provides most structural data: classes, datatype
properties, object properties, domains, ranges, inverse pairs, and datatype
ranges. `is_functional` was added because cardinality needed this missing fact.

## Violation Contract

- Use structured violations internally. Plain strings are not enough for
  feedback because the repair step needs subject, predicate, expected value, and
  actual value context.
- Normalize SHACL, reasoner, ontology mapping, and KG builder findings into one
  shared model.
- At minimum, a violation should include:
  - `kind`
  - `source`
  - `focus_node`
  - `path`
  - `message`
  - `severity`
- Sort violations deterministically before comparing or storing them. Plateau
  detection depends on stable ordering.
- Preserve the current API/DB `list[str]` surface if needed by converting
  structured violations to display strings at the boundary, not inside the
  validation core.
- `kind` values: `shacl`, `reasoner`, `unmapped_relation`, `dangling_reference`.
  `source` values: `shacl_generator`, `reasoner_runner`, `ontology_mapping`,
  `kg_builder`. The last two are diagnostics converted into violations, not
  produced by the SHACL/reasoner runners themselves.

### `focus_node` Resolution for Diagnostic-Sourced Violations

`unmapped_relation` and `dangling_reference` violations do not originate from an
existing triple, so `focus_node` cannot be resolved the same way as SHACL/reasoner
violations:

- `unmapped_relation` (source: `ontology_mapping`): `focus_node` is the subject
  entity's URI. The subject already exists in the graph (it was a listed
  extraction entity), so the "relevant focus-node triples" sent to the feedback
  agent are the subject's own existing triples, plus the `relation_phrase`, the
  candidate object URI, and the set of ontology predicates whose domain/range
  match the subject/object types (computed from the schema, not guessed by the
  LLM). The repair is a single `add_triple` once the correct predicate is chosen.
- `dangling_reference` (source: `kg_builder`): `focus_node` is the dangling
  entity's URI, which has no existing triples of its own. The "relevant triples"
  sent instead are the single relation triple that references it, plus the
  expected class for that entity position derived from the property's
  domain/range in the schema. The repair may need several `add_triple` calls
  (type first, then any attributes explicitly stated in the source text) — no
  separate `add_entity` op is needed since edit operations are already applied as
  a list per violation, not one-op-per-violation.

### `severity` Semantics

`severity` uses the same three levels as the SHACL spec: `violation`, `warning`,
`info`. This avoids inventing a separate aggregation rule for pySHACL's own
output, which already follows this convention.

- Only `severity == "violation"` findings gate the `conforms` decision that drives
  the `Complete` transition — matches pySHACL's own definition of `conforms`
  (no results at `sh:Violation` severity), so pySHACL's boolean can be used
  directly for SHACL-sourced findings without custom aggregation.
  `warning`/`info` findings do not block `Complete`.
- Reasoner-derived and diagnostic-derived (`unmapped_relation`,
  `dangling_reference`) violations must default to `severity = "violation"`, since
  they represent real defects, unless a later design explicitly downgrades a
  specific case.
- Plateau/oscillation comparison (see Pipeline Integration) still uses the full
  violation list regardless of severity — an unchanged `warning` across
  iterations is still evidence of no progress, even though it does not block
  completion on its own.
- No shape or diagnostic in the current MVP produces `warning`/`info`; the levels
  are reserved for future use (e.g. a heuristic check someone later wants to
  surface without blocking the job) and require no further pipeline changes when
  introduced.

## Feedback Contract

- Do not ask the LLM to rewrite full Turtle text.
- Feedback should return structured edit operations such as:
  - `add_triple`
  - `remove_triple`
  - `replace_literal`
- Apply edits with `rdflib` so Turtle syntax remains valid.
- Prompt the LLM with the violation list, the relevant focus-node triples, and
  the source text. Avoid sending the entire graph unless truly necessary.
- The LLM must not invent source facts. If a violation cannot be fixed from the
  source text, it should return no edit for that violation.
- A repair may emit more than one edit operation for a single violation.
  Reconstructing a `dangling_reference` entity, for example, means `add_triple`
  for `rdf:type` plus zero or more `add_triple` calls for attributes explicitly
  stated in the source text — all as part of the same repair.
- For `dangling_reference` violations specifically: if the source text does not
  clearly support the entity's existence or class, prefer `remove_triple` on the
  offending relation over inventing an `rdf:type` assertion. This is the concrete
  tie-breaker for the "must not invent source facts" rule when create-vs-delete is
  ambiguous.
- Log or record edit operations so reports can explain the iterative improvement
  process.

## Pipeline Integration

- Eventually move validation and feedback out of `tasks/pipeline_task.py` stubs:
  - `agents/validation_agent.py`
  - `agents/feedback_agent.py`
  - `validation/models.py`
  - `validation/shacl_generator.py`
  - `validation/shacl_runner.py`
  - `validation/reasoner_runner.py`
  - optional `validation/apply_edits.py`
- Pipeline iteration should eventually carry an `rdflib.Graph` rather than
  repeatedly serializing/deserializing Turtle strings.
- Only serialize to Turtle at final save boundaries or external API boundaries.
- Inject `ontology_mapping_agent` unmapped relations and `kg_builder_agent`
  dangling references into the validation loop as seed violations.
- Keep current termination modes:
  - conforms -> `Complete`
  - violation set repeats any earlier iteration in this job (not only the
    immediately preceding one) -> plateau `Error`
  - max iterations -> `MaxIterationsReached`
- Treat ontology/reasoner runtime failures as pipeline-level errors, not normal
  validation violations.

### Oscillation Detection

Comparing only against the immediately preceding iteration misses cycles (e.g.
A -> B -> A -> B), where a fix for one violation set reintroduces an earlier one.
Since `max_iterations` already bounds total iterations (default 10), comparing
each new iteration's (sorted, deterministic) violation list against the full set
of violation lists already seen in this job run costs at most O(max_iterations)
set comparisons — no separate window size is needed, and a fixed window would
still miss cycles longer than the window.

- Accumulate violation lists from each iteration in a local history list during
  the loop (parallel to what `add_iteration_detail` already persists per
  iteration; no new DB schema needed).
- On a repeat, record which earlier iteration matched and the resulting cycle
  length (`current_iteration - matched_iteration`) in `last_error`, so reports can
  distinguish an immediate plateau (cycle length 1) from a longer oscillation.

## Reasoner Constraints

- Use a fresh `owlready2.World()` per validation run/task. Do not share mutable
  reasoner world state across Celery workers.
- Expect coarse diagnostics from HermiT. It may identify inconsistency without a
  clean per-triple explanation.
- Add timeout protection around reasoner execution before using it in production
  iteration loops.
- Be mindful of Celery concurrency: multiple workers can spawn multiple JVM
  subprocesses. Revisit worker concurrency or separate reasoner queues if memory
  pressure appears.

## Testing Rules

- Keep tests ontology-agnostic where possible. Use mixed-domain fixtures, not
  only family ontology examples.
- Add family-specific tests only where the family ontology demonstrates a real
  OWL/SHACL distinction.
- Do not delete or overtrust `family_shapes.ttl`; some hand-written shapes may
  represent rules that dynamic SHACL should not hardcode and reasoner should
  eventually handle. See "Hand-Written Shape Supplements" for how/when it is
  merged into the SHACL graph.
- Each implementation step should be independently testable and mergeable.
- Run the full test suite before considering a day complete.
- For Docker/reasoner changes, verify inside the built image, not only locally.

## Current Roadmap

1. Schema loader + Docker/JRE.
2. `validation/models.py` + dynamic SHACL generator.
3. SHACL runner + pySHACL result normalization.
4. Reasoner prototype.
5. Reasoner runner + Docker validation + tests.
6. Validation agent orchestration.
7. Feedback agent edit operation generation. (implemented)
8. Apply edits + pipeline graph refactor. (implemented)
9. End-to-end Docker run, edge cases, README/report updates.

## Non-Negotiables

- Do not hardcode ontology-specific validation rules when the ontology can
  express them generically.
- Do not let LLM output directly replace the whole RDF graph.
- Do not ignore unmapped relations or dangling references as logs only.
- Do not allow nondeterministic violation ordering to break plateau/oscillation
  detection.
- Do not run HermiT in Docker without Java installed.
- Do not share owlready2 world state across jobs.
- Do not mark validation complete without tests proving the relevant layer.
