# Triple matching report: 711

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Lady_Jemima_Montagu | type | Agent |
| Lady_Jemima_Montagu | type | Person |
| Sir_Philip_Carteret_FRS | type | Agent |
| Sir_Philip_Carteret_FRS | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| George_Carteret_1st_Baron_Carteret | hasParent | Lady_Jemima_Montagu |
| George_Carteret_1st_Baron_Carteret | hasParent | Sir_Philip_Carteret_FRS |
| George_Carteret_1st_Baron_Carteret | type | Agent |
| George_Carteret_1st_Baron_Carteret | type | Person |
| Lady_Jemima_Montagu | hasChild | George_Carteret_1st_Baron_Carteret |
| Sir_Philip_Carteret_FRS | hasChild | George_Carteret_1st_Baron_Carteret |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Lady_Jemima_Montagu | hasSpouse | Sir_Philip_Carteret_FRS |
| Sir_Philip_Carteret_FRS | hasSpouse | Lady_Jemima_Montagu |

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
