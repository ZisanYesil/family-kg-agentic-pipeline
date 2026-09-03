# Triple matching report: 577

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Ernst_Düllberg | hasBirthDate | "1913-03-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ernst_Düllberg | hasDeathDate | "1984-07-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Louis_Antoine_Ranvier | hasBirthDate | "1835-10-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Louis_Antoine_Ranvier | hasDeathDate | "1922-03-22"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Ernst_Düllberg | type | Person |
| Ernst_Düllberg | type | NamedIndividual |
| Ernst_Düllberg | label | "Ernst Düllberg" |
| Louis_Antoine_Ranvier | type | Person |
| Louis_Antoine_Ranvier | type | NamedIndividual |
| Louis_Antoine_Ranvier | label | "Louis-Antoine Ranvier" |

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
