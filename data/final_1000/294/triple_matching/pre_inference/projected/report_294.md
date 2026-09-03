# Triple matching report: 294

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Douro_Wine_Company | hasFounder | Sebastião_José_de_Carvalho_e_Melo |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Sebastião_José_de_Carvalho_e_Melo | hasBirthPlace | Lisbon |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Douro_Wine_Company | type | Organization |
| Douro_Wine_Company | type | NamedIndividual |
| Douro_Wine_Company | label | "Douro Wine Company" |
| Sebastião_José_de_Carvalho_e_Melo | hasBirthDate | "1699-05-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sebastião_José_de_Carvalho_e_Melo | hasDeathDate | "1782-05-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sebastião_José_de_Carvalho_e_Melo | type | Person |
| Sebastião_José_de_Carvalho_e_Melo | type | NamedIndividual |
| Sebastião_José_de_Carvalho_e_Melo | label | "Sebastião José de Carvalho e Melo" |
| Sebastião_José_de_Carvalho_e_Melo | altLabel | "Marquis of Pombal" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.100000 |
| Recall | 0.500000 |
| F1 score | 0.166667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
