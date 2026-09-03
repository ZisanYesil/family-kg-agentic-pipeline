# Triple matching report: 149

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Arabia | hasParent | Sophia |
| Arabia | type | Agent |
| Arabia | type | Person |
| Sophia | hasChild | Arabia |
| Sophia | type | Agent |
| Sophia | type | Person |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Byzantine_Empire | type | Country |
| Byzantine_Empire | type | Place |
| Sophia | hasCountry | Byzantine_Empire |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 9 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 3 |
| Precision | 1.000000 |
| Recall | 0.666667 |
| F1 score | 0.800000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
