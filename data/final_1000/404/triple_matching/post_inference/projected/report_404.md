# Triple matching report: 404

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| David_Yow | hasBirthPlace | Las_Vegas_Nevada |
| David_Yow | type | Agent |
| David_Yow | type | Person |
| Las_Vegas_Nevada | type | Place |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Qui | hasMember | David_Yow |
| Qui | type | Agent |
| Qui | type | Organization |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 4 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 7 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 3 |
| Precision | 1.000000 |
| Recall | 0.571429 |
| F1 score | 0.727273 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
