# Triple matching report: 593

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| George_S_Patton | type | Agent |
| George_S_Patton | type | Person |
| Susan_Thornton_Glassell | type | Agent |
| Susan_Thornton_Glassell | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Col_George_Patton_Sr | hasChild | George_S_Patton |
| Col_George_Patton_Sr | type | Agent |
| Col_George_Patton_Sr | type | Person |
| George_S_Patton | hasParent | Col_George_Patton_Sr |
| George_S_Patton | hasParent | Susan_Thornton_Glassell |
| Susan_Thornton_Glassell | hasChild | George_S_Patton |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| George_S_Patton | hasSpouse | Susan_Thornton_Glassell |
| Susan_Thornton_Glassell | hasSpouse | George_S_Patton |

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
