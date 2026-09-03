# Final graph evaluation results

These results use the frozen 1,000-example cohort. The baseline is the original extracted graph. The final condition is the SHACL feedback output followed by ontology inference. One entity mapping is derived from each original extracted/ground-truth pair and applied to both conditions. Scoring projects equivalent family and country predicates and includes inferred `rdf:type` triples.

## Headline results

| Condition | Micro precision | Micro recall | Micro F1 | Macro F1 |
|---|---:|---:|---:|---:|
| Original extracted graphs | 17.1060% | 86.1689% | 28.5453% | 28.8341% |
| SHACL + inference graphs | 86.5868% | 91.8498% | 89.1407% | 88.6431% |
| Change | +69.4808 pp | +5.6810 pp | +60.5954 pp | +59.8090 pp |

The final condition contains 8,024 true positives, 1,243 false positives, and 712 false negatives. F1 increased for 993 examples, remained unchanged for 7, and decreased for none.

## Pipeline counts

| Stage | Result |
|---|---:|
| SHACL: no repair needed | 947 |
| SHACL: repaired | 20 |
| SHACL: unresolved | 33 |
| SHACL: failed | 0 |
| Inference completed | 1,000 |
| Inference failed | 0 |
| Accepted entity mappings | 2,731 |
| Entity review cases | 7 |
| Unmatched extracted entities | 139 |
| Unmatched ground-truth entities | 216 |

## Detailed outputs

- `final_results.json`: machine-readable consolidated snapshot.
- `entity_alignment_summary.json`: entity matching decisions and totals.
- `triple_matching_pre_inference_projected_summary.json`: complete baseline results.
- `triple_matching_post_inference_projected_summary.json`: complete final results.
- `triple_matching_inference_delta_projected.json`: paired per-example changes.
- `../shacl_summary.json`: SHACL feedback outcomes.
- `../inference_summary.json`: inference completion and graph-count audit.
