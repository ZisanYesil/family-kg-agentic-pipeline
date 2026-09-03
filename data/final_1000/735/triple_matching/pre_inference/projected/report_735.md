# Triple matching report: 735

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Alexander_Jeremiah_Orenstein | hasBirthDate | "1879-09-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Alexander_Jeremiah_Orenstein | hasDeathDate | "1972-07-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Lydia_Flood_Jackson | hasBirthDate | "1862-06-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Lydia_Flood_Jackson | hasDeathDate | "1963-07-08"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Alexander_Jeremiah_Orenstein | type | Person |
| Alexander_Jeremiah_Orenstein | type | NamedIndividual |
| Alexander_Jeremiah_Orenstein | label | "Alexander Jeremiah Orenstein" |
| Lydia_Flood_Jackson | type | Person |
| Lydia_Flood_Jackson | type | NamedIndividual |
| Lydia_Flood_Jackson | label | "Lydia Flood Jackson" |

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
