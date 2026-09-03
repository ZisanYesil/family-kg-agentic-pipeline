# Triple matching report: 401

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Moscow | type | Place |
| Nikolay_Novikov | hasDeathPlace | Moscow |
| Nikolay_Novikov | type | Agent |
| Nikolay_Novikov | type | Person |
| Truten | type | Artifact |
| Truten | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Truten | hasEditor | Nikolay_Novikov |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 7 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 1 |
| Precision | 1.000000 |
| Recall | 0.857143 |
| F1 score | 0.923077 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
