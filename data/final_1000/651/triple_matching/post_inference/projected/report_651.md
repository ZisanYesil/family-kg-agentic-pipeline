# Triple matching report: 651

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| New_York | type | Place |
| On_Moonlight_Bay | hasComposer | Percy_Wenrich |
| On_Moonlight_Bay | hasCreator | Percy_Wenrich |
| On_Moonlight_Bay | type | Artifact |
| On_Moonlight_Bay | type | CreativeWork |
| Percy_Wenrich | hasDeathPlace | New_York |
| Percy_Wenrich | type | Agent |
| Percy_Wenrich | type | Person |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| On_Moonlight_Bay | type | MusicalWork |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 9 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.888889 |
| Recall | 1.000000 |
| F1 score | 0.941176 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
