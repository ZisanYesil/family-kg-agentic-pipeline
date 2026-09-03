# Triple matching report: 898

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Carlos_F_Borcosque | hasBirthDate | "1894-09-09"^^<http://www.w3.org/2001/XMLSchema#date> |
| Cuando_en_el_cielo_pasen_lista | hasDirector | Carlos_F_Borcosque |
| Edward_Zwick | hasBirthDate | "1952-10-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Legends_of_the_Fall | hasDirector | Edward_Zwick |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Carlos_F_Borcosque | type | Person |
| Carlos_F_Borcosque | type | NamedIndividual |
| Carlos_F_Borcosque | label | "Carlos F. Borcosque" |
| Cuando_en_el_cielo_pasen_lista | type | Film |
| Cuando_en_el_cielo_pasen_lista | type | NamedIndividual |
| Cuando_en_el_cielo_pasen_lista | label | "Cuando en el cielo pasen lista" |
| Edward_Zwick | type | Person |
| Edward_Zwick | type | NamedIndividual |
| Edward_Zwick | label | "Edward Zwick" |
| Legends_of_the_Fall | type | Film |
| Legends_of_the_Fall | type | NamedIndividual |
| Legends_of_the_Fall | label | "Legends of the Fall" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 16 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
