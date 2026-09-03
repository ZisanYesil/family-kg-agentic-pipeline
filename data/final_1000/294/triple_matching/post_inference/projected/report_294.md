# Triple matching report: 294

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Douro_Wine_Company | hasFounder | Sebastião_José_de_Carvalho_e_Melo |
| Douro_Wine_Company | type | Agent |
| Douro_Wine_Company | type | Organization |
| Sebastião_José_de_Carvalho_e_Melo | type | Agent |
| Sebastião_José_de_Carvalho_e_Melo | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Lisbon | type | Place |
| Sebastião_José_de_Carvalho_e_Melo | hasBirthPlace | Lisbon |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Sebastião_José_de_Carvalho_e_Melo | hasBirthDate | "1699-05-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sebastião_José_de_Carvalho_e_Melo | hasDeathDate | "1782-05-08"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 9 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.714286 |
| Recall | 0.714286 |
| F1 score | 0.714286 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
