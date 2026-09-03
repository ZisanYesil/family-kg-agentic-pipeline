# Triple matching report: 453

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Esmé_Stewart_1st_Duke_of_Lennox | hasParent | Anne_de_la_Queuille |
| Esmé_Stewart_3rd_Duke_of_Lennox | hasParent | Esmé_Stewart_1st_Duke_of_Lennox |

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
| Anne_de_la_Queuille | type | Person |
| Anne_de_la_Queuille | type | NamedIndividual |
| Anne_de_la_Queuille | label | "Anne de la Queuille" |
| Esmé_Stewart_1st_Duke_of_Lennox | type | Person |
| Esmé_Stewart_1st_Duke_of_Lennox | type | NamedIndividual |
| Esmé_Stewart_1st_Duke_of_Lennox | label | "Esmé Stewart, 1st Duke of Lennox" |
| Esmé_Stewart_3rd_Duke_of_Lennox | type | Person |
| Esmé_Stewart_3rd_Duke_of_Lennox | type | NamedIndividual |
| Esmé_Stewart_3rd_Duke_of_Lennox | label | "Esmé Stewart, 3rd Duke of Lennox" |

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
