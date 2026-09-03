# Triple matching report: 531

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Laila_Kaland | hasBirthDate | "1939-01-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Laila_Kaland | hasDeathDate | "2007-12-30"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_F_Brown | hasBirthDate | "1919-11-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_F_Brown | hasDeathDate | "2010-09-06"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Laila_Kaland | type | Person |
| Laila_Kaland | type | NamedIndividual |
| Laila_Kaland | label | "Laila Kaland" |
| William_F_Brown | type | Person |
| William_F_Brown | type | NamedIndividual |
| William_F_Brown | label | "William F. Brown" |

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
