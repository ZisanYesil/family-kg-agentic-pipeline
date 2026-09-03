# Triple matching report: 912

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Pier_Celestino_Gilardi | hasBirthDate | "1837-09-16"^^<http://www.w3.org/2001/XMLSchema#date> |
| Robert_Heetmøller | hasBirthDate | "1950-06-28"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Pier_Celestino_Gilardi | type | Person |
| Pier_Celestino_Gilardi | type | NamedIndividual |
| Pier_Celestino_Gilardi | label | "Pier Celestino Gilardi" |
| Pier_Celestino_Gilardi | altLabel | "Pier Celestino Gilardi" |
| Robert_Heetmøller | type | Person |
| Robert_Heetmøller | type | NamedIndividual |
| Robert_Heetmøller | label | "Robert Heetmøller" |
| Robert_Heetmøller | altLabel | "Robert Heetmøller" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
