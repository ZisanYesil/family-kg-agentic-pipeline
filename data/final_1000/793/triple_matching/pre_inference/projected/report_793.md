# Triple matching report: 793

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Amanda_Ruter_Dufour | hasBirthDate | "1822-02-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Amanda_Ruter_Dufour | hasDeathDate | "1899-05-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Daniel_Agnew | hasBirthDate | "1809-01-05"^^<http://www.w3.org/2001/XMLSchema#date> |
| Daniel_Agnew | hasDeathDate | "1902-03-09"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Amanda_Ruter_Dufour | type | Person |
| Amanda_Ruter_Dufour | type | NamedIndividual |
| Amanda_Ruter_Dufour | label | "Amanda Ruter Dufour" |
| Daniel_Agnew | type | Person |
| Daniel_Agnew | type | NamedIndividual |
| Daniel_Agnew | label | "Daniel Agnew" |

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
