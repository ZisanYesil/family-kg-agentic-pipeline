# Triple matching report: 968

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Ben_Witherington_III | hasBirthDate | "1951-12-30"^^<http://www.w3.org/2001/XMLSchema#date> |
| Tra_Deon_Hollins | hasBirthDate | "1995-08-22"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Ben_Witherington_III | type | Person |
| Ben_Witherington_III | type | NamedIndividual |
| Ben_Witherington_III | label | "Ben Witherington III" |
| Tra_Deon_Hollins | type | Person |
| Tra_Deon_Hollins | type | NamedIndividual |
| Tra_Deon_Hollins | label | "Tra-Deon Hollins" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 8 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
