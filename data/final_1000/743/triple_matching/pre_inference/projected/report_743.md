# Triple matching report: 743

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Joseph_Pitton_de_Tournefort | hasBirthDate | "1656-06-05"^^<http://www.w3.org/2001/XMLSchema#date> |
| Joseph_Pitton_de_Tournefort | hasDeathDate | "1708-12-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Piotr_Wala | hasBirthDate | "1936-12-16"^^<http://www.w3.org/2001/XMLSchema#date> |
| Piotr_Wala | hasDeathDate | "2013-10-22"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Joseph_Pitton_de_Tournefort | type | Person |
| Joseph_Pitton_de_Tournefort | type | NamedIndividual |
| Joseph_Pitton_de_Tournefort | label | "Joseph Pitton de Tournefort" |
| Piotr_Wala | type | Person |
| Piotr_Wala | type | NamedIndividual |
| Piotr_Wala | label | "Piotr Wala" |

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
