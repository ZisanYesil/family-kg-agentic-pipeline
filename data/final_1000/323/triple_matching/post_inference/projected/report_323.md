# Triple matching report: 323

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| George_Charles_Wallich | type | Agent |
| George_Charles_Wallich | type | Person |
| Nathaniel_Wallich | type | Agent |
| Nathaniel_Wallich | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Calcutta_Botanical_Garden | type | Agent |
| Calcutta_Botanical_Garden | type | Organization |
| George_Charles_Wallich | hasParent | Nathaniel_Wallich |
| Nathaniel_Wallich | hasChild | George_Charles_Wallich |
| Nathaniel_Wallich | hasEmployer | Calcutta_Botanical_Garden |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| George_Charles_Wallich | hasChild | Nathaniel_Wallich |
| Nathaniel_Wallich | hasParent | George_Charles_Wallich |
| royal_botanical_gardens | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 5 |
| Precision | 0.571429 |
| Recall | 0.444444 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
