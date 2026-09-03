# Triple matching report: 938

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Eleonora_Luisa_Gonzaga | hasParent | Vincenzo_Gonzaga_Duke_of_Guastalla |
| Vincenzo_Gonzaga_Duke_of_Guastalla | hasParent | Andrea_Gonzaga |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Andrea_Gonzaga | type | Person |
| Andrea_Gonzaga | type | NamedIndividual |
| Andrea_Gonzaga | label | "Andrea Gonzaga" |
| Andrea_Gonzaga | altLabel | "Andrea Gonzaga, Count of San Paolo" |
| Eleonora_Luisa_Gonzaga | type | Person |
| Eleonora_Luisa_Gonzaga | type | NamedIndividual |
| Eleonora_Luisa_Gonzaga | label | "Eleonora Luisa Gonzaga" |
| Vincenzo_Gonzaga_Duke_of_Guastalla | type | Person |
| Vincenzo_Gonzaga_Duke_of_Guastalla | type | NamedIndividual |
| Vincenzo_Gonzaga_Duke_of_Guastalla | label | "Vincenzo Gonzaga" |
| Vincenzo_Gonzaga_Duke_of_Guastalla | altLabel | "Vincenzo Gonzaga, Duke of Guastalla" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
