# Triple matching report: 279

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Arati_Ankalikar_Tikekar | type | Agent |
| Arati_Ankalikar_Tikekar | type | Person |
| Uday_Tikekar | type | Agent |
| Uday_Tikekar | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Arati_Ankalikar_Tikekar | hasChild | Swanandi_Tikekar |
| Swanandi_Tikekar | hasParent | Arati_Ankalikar_Tikekar |
| Swanandi_Tikekar | hasParent | Uday_Tikekar |
| Swanandi_Tikekar | type | Agent |
| Swanandi_Tikekar | type | Person |
| Uday_Tikekar | hasChild | Swanandi_Tikekar |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Arati_Ankalikar_Tikekar | hasSpouse | Uday_Tikekar |
| Uday_Tikekar | hasSpouse | Arati_Ankalikar_Tikekar |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.666667 |
| Recall | 0.400000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
