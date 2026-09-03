# Triple matching report: 397

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Hans_Rosling | hasBirthDate | "1948-07-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Hans_Rosling | hasDeathDate | "2017-02-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Kınar_Sıvacıyan | hasBirthDate | "1876"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Kınar_Sıvacıyan | hasDeathDate | "1950-08-13"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Hans_Rosling | type | Person |
| Hans_Rosling | type | NamedIndividual |
| Hans_Rosling | label | "Hans Rosling" |
| Kınar_Sıvacıyan | type | Person |
| Kınar_Sıvacıyan | type | NamedIndividual |
| Kınar_Sıvacıyan | label | "Kınar Sıvacıyan" |
| Kınar_Sıvacıyan | altLabel | "Kınar Hanım" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 11 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.363636 |
| Recall | 1.000000 |
| F1 score | 0.533333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
