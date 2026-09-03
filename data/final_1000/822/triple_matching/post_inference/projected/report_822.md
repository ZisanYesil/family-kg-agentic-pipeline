# Triple matching report: 822

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Ang_Em | hasParent | Ang_Nan |
| Ang_Em | type | Agent |
| Ang_Em | type | Person |
| Ang_Nan | hasChild | Ang_Em |
| Ang_Nan | hasDeathPlace | Srey_Santhor |
| Ang_Nan | type | Agent |
| Ang_Nan | type | Person |
| Srey_Santhor | type | Place |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Ang_Em | hasBirthDate | "1674-01-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ang_Em | hasDeathDate | "1731-01-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ang_Nan | hasBirthDate | "1654-01-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ang_Nan | hasDeathDate | "1691-01-01"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 12 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.666667 |
| Recall | 1.000000 |
| F1 score | 0.800000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
