# Triple matching report: 16

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Antonio_González_Flores | hasParent | Lola_Flores |
| Lola_Flores | hasBirthPlace | Jerez_de_la_Frontera |

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
| Antonio_González_Flores | type | Person |
| Antonio_González_Flores | type | NamedIndividual |
| Antonio_González_Flores | label | "Antonio González Flores" |
| Antonio_González_Flores | altLabel | "Antonio Flores" |
| Jerez_de_la_Frontera | type | Place |
| Jerez_de_la_Frontera | type | NamedIndividual |
| Jerez_de_la_Frontera | label | "Jerez de la Frontera" |
| Lola_Flores | type | Person |
| Lola_Flores | type | NamedIndividual |
| Lola_Flores | label | "María Dolores Flores Ruiz" |
| Lola_Flores | altLabel | "Lola Flores" |

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
