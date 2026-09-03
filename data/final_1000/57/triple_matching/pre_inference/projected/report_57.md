# Triple matching report: 57

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Giuseppe_Diotti | hasBirthDate | "1779-03-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Giuseppe_Diotti | hasDeathDate | "1846-01-30"^^<http://www.w3.org/2001/XMLSchema#date> |
| Gustav_Philipp_Mörl | hasBirthDate | "1673-12-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Gustav_Philipp_Mörl | hasDeathDate | "1750-05-07"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Giuseppe_Diotti | type | Person |
| Giuseppe_Diotti | type | NamedIndividual |
| Giuseppe_Diotti | label | "Giuseppe Diotti" |
| Gustav_Philipp_Mörl | type | Person |
| Gustav_Philipp_Mörl | type | NamedIndividual |
| Gustav_Philipp_Mörl | label | "Gustav Philipp Mörl" |

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
