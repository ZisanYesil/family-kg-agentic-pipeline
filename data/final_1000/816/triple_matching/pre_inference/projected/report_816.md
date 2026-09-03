# Triple matching report: 816

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Albert_Terrien_de_Lacouperie | hasBirthDate | "1844-11-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Albert_Terrien_de_Lacouperie | hasDeathDate | "1894-10-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Gustav_von_Hüfner | hasBirthDate | "1840-05-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Gustav_von_Hüfner | hasDeathDate | "1908-03-14"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Albert_Terrien_de_Lacouperie | type | Person |
| Albert_Terrien_de_Lacouperie | type | NamedIndividual |
| Albert_Terrien_de_Lacouperie | label | "Albert Terrien de Lacouperie" |
| Albert_Terrien_de_Lacouperie | altLabel | "Albert Terrien de Lacouperie" |
| Albert_Terrien_de_Lacouperie | altLabel | "Albert Étienne Jean-Baptiste Terrien de Lacouperie" |
| Gustav_von_Hüfner | type | Person |
| Gustav_von_Hüfner | type | NamedIndividual |
| Gustav_von_Hüfner | label | "Gustav von Hüfner" |
| Gustav_von_Hüfner | altLabel | "Gustav von Hüfner" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 13 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.307692 |
| Recall | 1.000000 |
| F1 score | 0.470588 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
