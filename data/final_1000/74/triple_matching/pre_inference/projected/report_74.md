# Triple matching report: 74

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Princess_Alice_of_Battenberg | hasDeathPlace | Buckingham_Palace |
| Princess_Margarita_of_Greece_and_Denmark | hasParent | Princess_Alice_of_Battenberg |

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
| Buckingham_Palace | type | Place |
| Buckingham_Palace | type | NamedIndividual |
| Buckingham_Palace | label | "Buckingham Palace" |
| Princess_Alice_of_Battenberg | type | Person |
| Princess_Alice_of_Battenberg | type | NamedIndividual |
| Princess_Alice_of_Battenberg | label | "Princess Alice of Battenberg" |
| Princess_Margarita_of_Greece_and_Denmark | type | Person |
| Princess_Margarita_of_Greece_and_Denmark | type | NamedIndividual |
| Princess_Margarita_of_Greece_and_Denmark | label | "Princess Margarita of Greece and Denmark" |

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
