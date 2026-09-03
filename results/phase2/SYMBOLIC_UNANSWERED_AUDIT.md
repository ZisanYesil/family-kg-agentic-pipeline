# Symbolic Unanswered-Case Audit

## Outcome

After adding a conservative, ground-truth-free anchor fallback, the symbolic system
returns answers for 887 of 1,000 examples. Unanswered cases decreased from 122 to 113,
while compatible correction increased from 78.70% to 79.50%. The fallback changed nine
previously empty results and produced eight benchmark-compatible answers. It uses only
question tokens and graph labels/aliases.

## Remaining 113 cases

| Retrieval outcome | Cases | Interpretation |
|---|---:|---|
| No reachable candidate path | 71 | The selected anchor has no one/two-hop path matching the supplied relation chain. |
| Insufficient comparable values | 19 | A comparison cannot be completed because at least one branch lacks a resolvable value. |
| Insufficient anchors | 9 | A two-entity comparison does not resolve both entities from graph labels or aliases. |
| No anchor | 6 | No sufficiently reliable graph entity corresponds to the question mention. |
| Paths exist but predicates do not match | 8 | Candidate paths use semantically different predicates, such as education versus employment or founder versus performer. |

Question-type distribution:

| Type | Unanswered |
|---|---:|
| Compositional | 70 |
| Comparison | 22 |
| Inference | 15 |
| Bridge comparison | 6 |

In 63 of the 113 cases, no label, alias, or literal compatible with the reference answer
appears anywhere in the reasoned extracted graph. These are graph-content coverage
failures and cannot be repaired by query traversal alone. In the other 50, the answer
surface occurs somewhere in the graph, but this does not establish that a valid path from
the question anchor to that value exists.

## Changes deliberately rejected

The resolver does not equate semantically different predicates merely to increase answer
coverage. Examples include treating `hasEducatedAt` as `hasEmployer`, `hasFounder` as a
performer/member relation, or `hasPresenter` as `hasCreator`. Such substitutions could
return the reference entity accidentally while failing to answer the stated relation.

Further coverage would require one or more separately evaluated changes:

- Improve graph extraction so missing relation paths are present before reasoning.
- Expand source-grounded entity aliases for the six unresolved anchors.
- Improve two-entity anchor recognition for comparison questions.
- Add a question-guided extraction pass applied consistently to the entire cohort.
- Add a text fallback, explicitly reported as a hybrid graph-plus-text condition rather
  than pure symbolic graph QA.

The 113 empty answers remain in the primary denominator and receive zero correctness and
zero token F1.
