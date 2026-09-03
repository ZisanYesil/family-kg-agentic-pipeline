# Triple matching report: 440

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| John_Manners_Sutton | hasParent | Lord_George_Manners_Sutton |
| John_Manners_Sutton | type | Agent |
| John_Manners_Sutton | type | Person |
| Lord_George_Manners_Sutton | hasChild | John_Manners_Sutton |
| Lord_George_Manners_Sutton | type | Agent |
| Lord_George_Manners_Sutton | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Lord_George_Manners_Sutton | hasSibling | Lord_Robert_Manners_Sutton |
| Lord_Robert_Manners_Sutton | hasSibling | Lord_George_Manners_Sutton |
| Lord_Robert_Manners_Sutton | type | Agent |
| Lord_Robert_Manners_Sutton | type | Person |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Lord_George_Manners_Sutton | hasSibling | john_manners_marquess_of_granby |
| john_manners_marquess_of_granby | hasSibling | Lord_George_Manners_Sutton |
| john_manners_marquess_of_granby | type | Agent |
| john_manners_marquess_of_granby | type | Person |

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
