# Triple matching report: 398

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Bonne_of_Berry | type | Agent |
| Bonne_of_Berry | type | Person |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Bonne_of_Berry | hasChild | Felix_V |
| Bonne_of_Berry | hasCountry | France |
| Felix_V | hasParent | Bonne_of_Berry |
| Felix_V | type | Agent |
| Felix_V | type | Person |
| France | type | Country |
| France | type | Place |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Bonne_of_Berry | hasParent | amadeus_viii |
| amadeus_viii | hasChild | Bonne_of_Berry |
| amadeus_viii | type | Agent |
| amadeus_viii | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 1 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 7 |
| Precision | 0.333333 |
| Recall | 0.222222 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
