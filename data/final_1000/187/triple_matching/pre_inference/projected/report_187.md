# Triple matching report: 187

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Bruce_Cummins | hasBirthDate | "1929-11-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Bruce_Cummins | hasDeathDate | "2017-08-22"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ko_Tun_hwa | hasBirthDate | "1921-09-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ko_Tun_hwa | hasDeathDate | "2010-06-12"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Bruce_Cummins | type | Person |
| Bruce_Cummins | type | NamedIndividual |
| Bruce_Cummins | label | "Bruce Cummins" |
| Ko_Tun_hwa | type | Person |
| Ko_Tun_hwa | type | NamedIndividual |
| Ko_Tun_hwa | label | "Ko Tun-Hwa" |
| Ko_Tun_hwa | altLabel | "Vice Admiral Ko Tun-hwa" |

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
