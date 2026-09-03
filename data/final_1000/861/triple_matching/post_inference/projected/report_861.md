# Triple matching report: 861

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| George_I_of_Greece | hasChild | Prince_Christopher_of_Greece_and_Denmark |
| George_I_of_Greece | type | Agent |
| George_I_of_Greece | type | Person |
| Prince_Christopher_of_Greece_and_Denmark | hasParent | George_I_of_Greece |
| Prince_Christopher_of_Greece_and_Denmark | type | Agent |
| Prince_Christopher_of_Greece_and_Denmark | type | Person |
| Thessaloniki | type | Place |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| George_I | hasDeathPlace | Thessaloniki |
| George_I | type | Agent |
| George_I | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| George_I_of_Greece | hasDeathPlace | Thessaloniki |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 11 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.875000 |
| Recall | 0.700000 |
| F1 score | 0.777778 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
