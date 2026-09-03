# Triple matching report: 809

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Shriro | hasInception | "1906"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| TJ_Ryan_Foundation | hasInception | "2014-02-27"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Shriro | type | Organization |
| Shriro | type | NamedIndividual |
| Shriro | label | "Shriro" |
| TJ_Ryan_Foundation | hasInception | "2012-05-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| TJ_Ryan_Foundation | type | Organization |
| TJ_Ryan_Foundation | type | NamedIndividual |
| TJ_Ryan_Foundation | label | "TJ Ryan Foundation" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.125000 |
| Recall | 0.500000 |
| F1 score | 0.200000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
