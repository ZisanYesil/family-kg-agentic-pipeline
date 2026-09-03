# Triple matching report: 777

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Isabel_de_la_Cerda | hasParent | Luis_de_la_Cerda |
| Luis_de_la_Cerda | hasBirthPlace | France |

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
| France | type | Country |
| France | type | NamedIndividual |
| France | label | "France" |
| France | altLabel | "France" |
| Isabel_de_la_Cerda | type | Person |
| Isabel_de_la_Cerda | type | NamedIndividual |
| Isabel_de_la_Cerda | label | "Isabel de la Cerda" |
| Isabel_de_la_Cerda | altLabel | "Isabel de la Cerda Pérez de Guzmán" |
| Luis_de_la_Cerda | type | Person |
| Luis_de_la_Cerda | type | NamedIndividual |
| Luis_de_la_Cerda | label | "Luis de la Cerda" |

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
