# Triple matching report: 694

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Aregund | hasChild | Chilperic_I |
| Aregund | type | Agent |
| Aregund | type | Person |
| Chilperic_I | hasParent | Aregund |
| Chilperic_I | hasSpouse | Fredegund |
| Chilperic_I | type | Agent |
| Chilperic_I | type | Person |
| Fredegund | hasSpouse | Chilperic_I |
| Fredegund | type | Agent |
| Fredegund | type | Person |

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
| Fredegund | hasDeathDate | "0597-12-08"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 11 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.909091 |
| Recall | 1.000000 |
| F1 score | 0.952381 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
