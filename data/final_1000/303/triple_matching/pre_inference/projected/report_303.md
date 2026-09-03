# Triple matching report: 303

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Adelaide_of_Auxerre | hasParent | Conrad_II_Duke_of_Transjurane_Burgundy |
| Rudolph_of_France | hasParent | Adelaide_of_Auxerre |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Adelaide_of_Auxerre | type | Person |
| Adelaide_of_Auxerre | type | NamedIndividual |
| Adelaide_of_Auxerre | label | "Adelaide of Auxerre" |
| Conrad_II_Duke_of_Transjurane_Burgundy | type | Person |
| Conrad_II_Duke_of_Transjurane_Burgundy | type | NamedIndividual |
| Conrad_II_Duke_of_Transjurane_Burgundy | label | "Conrad II, Duke of Transjurane Burgundy" |
| Rudolph_of_France | type | Person |
| Rudolph_of_France | type | NamedIndividual |
| Rudolph_of_France | label | "Rudolph of France" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
