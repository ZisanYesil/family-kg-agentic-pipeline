# Triple matching report: 220

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Lady_Charlotte_Finch | hasParent | Thomas_Fermor |
| Lady_Charlotte_Finch | type | Agent |
| Lady_Charlotte_Finch | type | Person |
| Lady_Sophia_Osborne | type | Agent |
| Lady_Sophia_Osborne | type | Person |
| Thomas_Fermor | hasChild | Lady_Charlotte_Finch |
| Thomas_Fermor | type | Agent |
| Thomas_Fermor | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Lady_Sophia_Osborne | hasChild | Thomas_Fermor_1st_Earl_of_Pomfret |
| Thomas_Fermor_1st_Earl_of_Pomfret | hasParent | Lady_Sophia_Osborne |
| Thomas_Fermor_1st_Earl_of_Pomfret | type | Agent |
| Thomas_Fermor_1st_Earl_of_Pomfret | type | Person |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Lady_Sophia_Osborne | hasChild | Thomas_Fermor |
| Thomas_Fermor | hasParent | Lady_Sophia_Osborne |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 14 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.800000 |
| Recall | 0.666667 |
| F1 score | 0.727273 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
