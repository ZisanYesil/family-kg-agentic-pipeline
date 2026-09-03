# Triple matching report: 150

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Bruce_Guthro | hasBirthPlace | Cape_Breton_Island |
| Bruce_Guthro | type | Agent |
| Bruce_Guthro | type | Person |
| Cape_Breton_Island | type | Place |
| Falling | hasCreator | Bruce_Guthro |
| Falling | hasPerformer | Bruce_Guthro |
| Falling | type | Artifact |
| Falling | type | CreativeWork |

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
| Falling | type | MusicalWork |

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
