# Triple matching report: 180

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Hermann_Muthesius | hasBirthDate | "1861-04-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Hermann_Muthesius | hasDeathDate | "1927-10-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Kiril_Makedonski | hasBirthDate | "1925-01-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Kiril_Makedonski | hasDeathDate | "1984-06-02"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Hermann_Muthesius | type | Person |
| Hermann_Muthesius | type | NamedIndividual |
| Hermann_Muthesius | label | "Hermann Muthesius" |
| Kiril_Makedonski | type | Person |
| Kiril_Makedonski | type | NamedIndividual |
| Kiril_Makedonski | label | "Kiril Makedonski" |

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
