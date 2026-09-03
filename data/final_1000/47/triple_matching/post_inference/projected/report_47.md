# Triple matching report: 47

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Akiko_Matsuura | type | Agent |
| Akiko_Matsuura | type | Person |
| Japan | type | Country |
| Japan | type | Place |
| Pre | hasMember | Akiko_Matsuura |
| Pre | type | Agent |
| Pre | type | Organization |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Akiko_Matsuura | hasCountry | Japan |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Akiko_Matsuura | hasBirthPlace | osaka |
| osaka | hasCountry | Japan |
| osaka | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 11 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.700000 |
| Recall | 0.875000 |
| F1 score | 0.777778 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
