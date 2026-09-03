# Triple matching report: 158

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| John_the_Fearless | hasChild | Mary_of_Burgundy_Duchess_of_Cleves |
| John_the_Fearless | type | Agent |
| John_the_Fearless | type | Person |
| Marie_of_Cleves_Duchess_of_Orléans | type | Agent |
| Marie_of_Cleves_Duchess_of_Orléans | type | Person |
| Mary_of_Burgundy_Duchess_of_Cleves | hasParent | John_the_Fearless |
| Mary_of_Burgundy_Duchess_of_Cleves | type | Agent |
| Mary_of_Burgundy_Duchess_of_Cleves | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Marie_of_Burgundy | hasChild | Marie_of_Cleves_Duchess_of_Orléans |
| Marie_of_Burgundy | type | Agent |
| Marie_of_Burgundy | type | Person |
| Marie_of_Cleves_Duchess_of_Orléans | hasParent | Marie_of_Burgundy |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Marie_of_Cleves_Duchess_of_Orléans | hasParent | Mary_of_Burgundy_Duchess_of_Cleves |
| Mary_of_Burgundy_Duchess_of_Cleves | hasChild | Marie_of_Cleves_Duchess_of_Orléans |

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
