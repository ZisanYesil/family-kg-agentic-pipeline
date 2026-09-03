# Triple matching report: 282

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Prince_Foulques_of_Orléans_Duke_of_Aumale | hasParent | Prince_Jacques_Duke_of_Orléans |
| Prince_Jacques_Duke_of_Orléans | hasParent | Princess_Isabelle_of_Orléans_Braganza |

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
| Prince_Foulques_of_Orléans_Duke_of_Aumale | type | Person |
| Prince_Foulques_of_Orléans_Duke_of_Aumale | type | NamedIndividual |
| Prince_Foulques_of_Orléans_Duke_of_Aumale | label | "Prince Foulques of Orléans, Duke of Aumale" |
| Prince_Jacques_Duke_of_Orléans | type | Person |
| Prince_Jacques_Duke_of_Orléans | type | NamedIndividual |
| Prince_Jacques_Duke_of_Orléans | label | "Prince Jacques of Orléans, Duke of Orléans" |
| Princess_Isabelle_of_Orléans_Braganza | type | Person |
| Princess_Isabelle_of_Orléans_Braganza | type | NamedIndividual |
| Princess_Isabelle_of_Orléans_Braganza | label | "Princess Isabelle of Orléans-Braganza" |

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
