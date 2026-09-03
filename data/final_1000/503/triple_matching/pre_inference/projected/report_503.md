# Triple matching report: 503

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| André_Testut | hasBirthDate | "1926-04-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| André_Testut | hasDeathDate | "2005-09-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| Kurt_Cuno | hasBirthDate | "1896-08-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Kurt_Cuno | hasDeathDate | "1961-07-14"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| André_Testut | type | Person |
| André_Testut | type | NamedIndividual |
| André_Testut | label | "André Testut" |
| Kurt_Cuno | type | Person |
| Kurt_Cuno | type | NamedIndividual |
| Kurt_Cuno | label | "Kurt Cuno" |

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
