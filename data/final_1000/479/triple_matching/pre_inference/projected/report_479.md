# Triple matching report: 479

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Anthony_Crosland | hasBirthDate | "1918-08-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Anthony_Crosland | hasDeathDate | "1977-02-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Douglas_Vautin | hasBirthDate | "1896-07-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Douglas_Vautin | hasDeathDate | "1976-01-11"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Anthony_Crosland | type | Person |
| Anthony_Crosland | type | NamedIndividual |
| Anthony_Crosland | label | "Anthony Crosland" |
| Anthony_Crosland | altLabel | "C. A. R. Crosland" |
| Anthony_Crosland | altLabel | "Charles Anthony Raven Crosland" |
| Anthony_Crosland | altLabel | "Tony Crosland" |
| Douglas_Vautin | type | Person |
| Douglas_Vautin | type | NamedIndividual |
| Douglas_Vautin | label | "Douglas Vautin" |

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
