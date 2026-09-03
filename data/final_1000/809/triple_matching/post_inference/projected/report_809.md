# Triple matching report: 809

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Shriro | hasInception | "1906"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Shriro | type | Agent |
| Shriro | type | Organization |
| TJ_Ryan_Foundation | type | Agent |
| TJ_Ryan_Foundation | type | Organization |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| TJ_Ryan_Foundation | hasInception | "2014-02-27"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| TJ_Ryan_Foundation | hasInception | "2012-05-04"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 7 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.833333 |
| Recall | 0.833333 |
| F1 score | 0.833333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
