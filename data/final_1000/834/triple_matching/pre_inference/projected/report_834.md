# Triple matching report: 834

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Lee_Mantle | hasBirthDate | "1851-12-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Lee_Mantle | hasDeathDate | "1934-11-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Silas_Hardy | hasBirthDate | "1867-04-30"^^<http://www.w3.org/2001/XMLSchema#date> |
| Silas_Hardy | hasDeathDate | "1905-06-27"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Lee_Mantle | type | Person |
| Lee_Mantle | type | NamedIndividual |
| Lee_Mantle | label | "Lee Mantle" |
| Silas_Hardy | type | Person |
| Silas_Hardy | type | NamedIndividual |
| Silas_Hardy | label | "Silas Hardy" |

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
