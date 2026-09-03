# Triple matching report: 273

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Margaret_Holles_Duchess_of_Newcastle_upon_Tyne | type | Agent |
| Margaret_Holles_Duchess_of_Newcastle_upon_Tyne | type | Person |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| John_Holles_1st_Duke_of_Newcastle | hasChild | Lady_Henrietta_Cavendish_Holles |
| John_Holles_1st_Duke_of_Newcastle | type | Agent |
| John_Holles_1st_Duke_of_Newcastle | type | Person |
| Lady_Henrietta_Cavendish_Holles | hasParent | John_Holles_1st_Duke_of_Newcastle |
| Lady_Henrietta_Cavendish_Holles | hasParent | Margaret_Holles_Duchess_of_Newcastle_upon_Tyne |
| Lady_Henrietta_Cavendish_Holles | type | Agent |
| Lady_Henrietta_Cavendish_Holles | type | Person |
| Margaret_Holles_Duchess_of_Newcastle_upon_Tyne | hasChild | Lady_Henrietta_Cavendish_Holles |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Margaret_Holles_Duchess_of_Newcastle_upon_Tyne | hasSpouse | john_holles |
| john_holles | hasSpouse | Margaret_Holles_Duchess_of_Newcastle_upon_Tyne |
| john_holles | type | Agent |
| john_holles | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 1 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 8 |
| Precision | 0.333333 |
| Recall | 0.200000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
