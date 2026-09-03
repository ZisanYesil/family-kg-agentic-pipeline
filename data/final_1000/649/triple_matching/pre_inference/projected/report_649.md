# Triple matching report: 649

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Iraj_Kiarostami | hasBirthDate | "1963-07-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Iraj_Kiarostami | hasDeathDate | "2015-08-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Joseph_Peyré | hasBirthDate | "1892-03-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Joseph_Peyré | hasDeathDate | "1968-12-26"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Iraj_Kiarostami | type | Person |
| Iraj_Kiarostami | type | NamedIndividual |
| Iraj_Kiarostami | label | "Iraj Kiarostami" |
| Joseph_Peyré | type | Person |
| Joseph_Peyré | type | NamedIndividual |
| Joseph_Peyré | label | "Joseph Peyré" |

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
