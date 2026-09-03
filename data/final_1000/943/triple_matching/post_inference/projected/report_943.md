# Triple matching report: 943

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Elizabeth_Fitzalan_Duchess_of_Norfolk | type | Agent |
| Elizabeth_Fitzalan_Duchess_of_Norfolk | type | Person |
| Thomas_de_Mowbray_1st_Duke_of_Norfolk | hasDeathPlace | Venice |
| Thomas_de_Mowbray_1st_Duke_of_Norfolk | type | Agent |
| Thomas_de_Mowbray_1st_Duke_of_Norfolk | type | Person |
| Venice | type | Place |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Elizabeth_Fitzalan_Duchess_of_Norfolk | hasSpouse | Thomas_Mowbray |
| Thomas_Mowbray | hasSpouse | Elizabeth_Fitzalan_Duchess_of_Norfolk |
| Thomas_Mowbray | type | Agent |
| Thomas_Mowbray | type | Person |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Elizabeth_Fitzalan_Duchess_of_Norfolk | hasSpouse | Thomas_de_Mowbray_1st_Duke_of_Norfolk |
| Thomas_de_Mowbray_1st_Duke_of_Norfolk | hasSpouse | Elizabeth_Fitzalan_Duchess_of_Norfolk |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 12 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.750000 |
| Recall | 0.600000 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
