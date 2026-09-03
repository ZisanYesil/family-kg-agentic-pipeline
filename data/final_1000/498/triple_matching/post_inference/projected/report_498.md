# Triple matching report: 498

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Augustus_Henry_Seward | hasParent | Frances_Adeline_Seward |
| Augustus_Henry_Seward | type | Agent |
| Augustus_Henry_Seward | type | Person |
| Frances_Adeline_Seward | hasChild | Augustus_Henry_Seward |
| Frances_Adeline_Seward | hasDeathDate | "1865-06-21"^^<http://www.w3.org/2001/XMLSchema#date> |
| Frances_Adeline_Seward | type | Agent |
| Frances_Adeline_Seward | type | Person |

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
| Frances_Adeline_Seward | hasBirthDate | "1805-09-25"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 8 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.875000 |
| Recall | 1.000000 |
| F1 score | 0.933333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
