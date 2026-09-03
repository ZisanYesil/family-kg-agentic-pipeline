# Triple matching report: 184

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Ladislav_Stroupežnický | hasBirthDate | "1850-01-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ladislav_Stroupežnický | hasDeathDate | "1892-08-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Peder_Mørk_Mønsted | hasBirthDate | "1859-12-10"^^<http://www.w3.org/2001/XMLSchema#date> |
| Peder_Mørk_Mønsted | hasDeathDate | "1941-06-20"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Ladislav_Stroupežnický | type | Person |
| Ladislav_Stroupežnický | type | NamedIndividual |
| Ladislav_Stroupežnický | label | "Ladislav Stroupežnický" |
| Peder_Mørk_Mønsted | type | Person |
| Peder_Mørk_Mønsted | type | NamedIndividual |
| Peder_Mørk_Mønsted | label | "Peder Mørk Mønsted" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 10 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.400000 |
| Recall | 1.000000 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
