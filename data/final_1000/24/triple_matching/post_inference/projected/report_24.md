# Triple matching report: 24

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Hugh_de_Stafford_2nd_Earl_of_Stafford | type | Agent |
| Hugh_de_Stafford_2nd_Earl_of_Stafford | type | Person |
| Thomas_Stafford_3rd_Earl_of_Stafford | type | Agent |
| Thomas_Stafford_3rd_Earl_of_Stafford | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Hugh_de_Stafford_2nd_Earl_of_Stafford | hasSpouse | Philippa_de_Beauchamp |
| Philippa_de_Beauchamp | hasChild | Thomas_Stafford_3rd_Earl_of_Stafford |
| Philippa_de_Beauchamp | hasSpouse | Hugh_de_Stafford_2nd_Earl_of_Stafford |
| Philippa_de_Beauchamp | type | Agent |
| Philippa_de_Beauchamp | type | Person |
| Thomas_Stafford_3rd_Earl_of_Stafford | hasParent | Philippa_de_Beauchamp |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Hugh_de_Stafford_2nd_Earl_of_Stafford | hasChild | Thomas_Stafford_3rd_Earl_of_Stafford |
| Thomas_Stafford_3rd_Earl_of_Stafford | hasParent | Hugh_de_Stafford_2nd_Earl_of_Stafford |

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
