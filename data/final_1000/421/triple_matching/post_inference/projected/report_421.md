# Triple matching report: 421

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Bob_Graham | hasChild | Gwendolyn_Graham |
| Bob_Graham | type | Agent |
| Bob_Graham | type | Person |
| Gwendolyn_Graham | hasParent | Bob_Graham |
| Gwendolyn_Graham | type | Agent |
| Gwendolyn_Graham | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Bob_Graham | hasEmployer | Harvard |
| Harvard | type | Agent |
| Harvard | type | Organization |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Bob_Graham | hasEmployer | bob_graham_center |
| bob_graham_center | type | Agent |
| bob_graham_center | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 12 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.666667 |
| Recall | 0.666667 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
