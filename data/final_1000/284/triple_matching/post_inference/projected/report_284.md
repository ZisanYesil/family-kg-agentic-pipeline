# Triple matching report: 284

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Dmitri_Nikolaevich_Sheremetev | hasParent | Nikolai_Sheremetev |
| Dmitri_Nikolaevich_Sheremetev | type | Agent |
| Dmitri_Nikolaevich_Sheremetev | type | Person |
| Nikolai_Sheremetev | hasChild | Dmitri_Nikolaevich_Sheremetev |
| Nikolai_Sheremetev | type | Agent |
| Nikolai_Sheremetev | type | Person |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Moscow | type | Place |
| Nikolai_Sheremetev | hasDeathPlace | Moscow |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 2 |
| Precision | 1.000000 |
| Recall | 0.750000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
