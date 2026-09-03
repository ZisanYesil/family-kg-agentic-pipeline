# Triple matching report: 707

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Charles_IV | hasChild | Elisabeth_of_Bohemia |
| Charles_IV | type | Agent |
| Charles_IV | type | Person |
| Elisabeth_of_Bohemia | hasParent | Charles_IV |
| Elisabeth_of_Bohemia | type | Agent |
| Elisabeth_of_Bohemia | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Charles_IV | hasParent | Elizabeth_of_Bohemia |
| Elizabeth_of_Bohemia | hasChild | Charles_IV |
| Elizabeth_of_Bohemia | type | Agent |
| Elizabeth_of_Bohemia | type | Person |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Charles_IV | hasParent | elisabeth_of_bohemia_1292 |
| elisabeth_of_bohemia_1292 | hasChild | Charles_IV |
| elisabeth_of_bohemia_1292 | type | Agent |
| elisabeth_of_bohemia_1292 | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 14 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.600000 |
| Recall | 0.600000 |
| F1 score | 0.600000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
