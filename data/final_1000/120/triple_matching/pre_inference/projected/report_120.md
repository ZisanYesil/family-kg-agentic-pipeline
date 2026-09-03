# Triple matching report: 120

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Mahisente_Habte_Mariam | hasSpouse | Prince_Sahle_Selassie |
| Prince_Sahle_Selassie | hasParent | Menen_Asfaw |

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
| Mahisente_Habte_Mariam | type | Person |
| Mahisente_Habte_Mariam | type | NamedIndividual |
| Mahisente_Habte_Mariam | label | "Mahisente Habte Mariam" |
| Menen_Asfaw | type | Person |
| Menen_Asfaw | type | NamedIndividual |
| Menen_Asfaw | label | "Empress Menen Asfaw" |
| Prince_Sahle_Selassie | type | Person |
| Prince_Sahle_Selassie | type | NamedIndividual |
| Prince_Sahle_Selassie | label | "Prince Sahle Selassie" |

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
