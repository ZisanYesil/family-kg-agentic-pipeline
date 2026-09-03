# Triple matching report: 240

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Bronislav_Gimpel | hasBirthDate | "1911-01-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Bronislav_Gimpel | hasDeathDate | "1979-05-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Lilavati_Singh | hasBirthDate | "1868-12-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Lilavati_Singh | hasDeathDate | "1909-05-09"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Bronislav_Gimpel | type | Person |
| Bronislav_Gimpel | type | NamedIndividual |
| Bronislav_Gimpel | label | "Bronislav Gimpel" |
| Lilavati_Singh | type | Person |
| Lilavati_Singh | type | NamedIndividual |
| Lilavati_Singh | label | "Lilavati Singh" |
| Lilavati_Singh | altLabel | "Lilivati Singh" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 11 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.363636 |
| Recall | 1.000000 |
| F1 score | 0.533333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
