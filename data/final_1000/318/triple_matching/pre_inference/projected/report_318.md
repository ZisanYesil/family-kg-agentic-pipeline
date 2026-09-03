# Triple matching report: 318

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| La_Estancia_de_gaucho_Cruz | hasDirector | Leopoldo_Torres_Rios |
| Leopoldo_Torres_Rios | hasChild | Leopoldo_Torre_Nilsson |

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
| La_Estancia_de_gaucho_Cruz | type | Film |
| La_Estancia_de_gaucho_Cruz | type | NamedIndividual |
| La_Estancia_de_gaucho_Cruz | label | "La Estancia de gaucho Cruz" |
| Leopoldo_Torre_Nilsson | type | Person |
| Leopoldo_Torre_Nilsson | type | NamedIndividual |
| Leopoldo_Torre_Nilsson | label | "Leopoldo Torre Nilsson" |
| Leopoldo_Torres_Rios | type | Person |
| Leopoldo_Torres_Rios | type | NamedIndividual |
| Leopoldo_Torres_Rios | label | "Leopoldo Torres Rios" |

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
