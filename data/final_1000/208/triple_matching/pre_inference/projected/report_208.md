# Triple matching report: 208

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Gebhard_Fugel | hasBirthDate | "1863-08-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Gebhard_Fugel | hasDeathDate | "1939-02-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Marcin_Kasprzak | hasBirthDate | "1860-11-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Marcin_Kasprzak | hasDeathDate | "1905-09-08"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Gebhard_Fugel | type | Person |
| Gebhard_Fugel | type | NamedIndividual |
| Gebhard_Fugel | label | "Gebhard Fugel" |
| Marcin_Kasprzak | type | Person |
| Marcin_Kasprzak | type | NamedIndividual |
| Marcin_Kasprzak | label | "Marcin Kasprzak" |

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
