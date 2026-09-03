# Triple matching report: 720

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Arthur_MacArthur_IV | type | Agent |
| Arthur_MacArthur_IV | type | Person |
| Douglas_MacArthur | hasCountry | American |
| Douglas_MacArthur | type | Agent |
| Douglas_MacArthur | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_MacArthur_IV | hasParent | Douglas_MacArthur |
| Douglas_MacArthur | hasChild | Arthur_MacArthur_IV |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_MacArthur_IV | hasChild | Douglas_MacArthur |
| Douglas_MacArthur | hasParent | Arthur_MacArthur_IV |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 11 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.777778 |
| Recall | 0.777778 |
| F1 score | 0.777778 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
