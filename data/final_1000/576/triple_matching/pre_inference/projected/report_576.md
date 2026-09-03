# Triple matching report: 576

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Franz_Limmer | hasBirthDate | "1808-10-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Franz_Limmer | hasDeathDate | "1857-01-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Robert_Glen_Coe | hasBirthDate | "1956-04-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| Robert_Glen_Coe | hasDeathDate | "2000-04-19"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Franz_Limmer | type | Person |
| Franz_Limmer | type | NamedIndividual |
| Franz_Limmer | label | "Franz Limmer" |
| Robert_Glen_Coe | type | Person |
| Robert_Glen_Coe | type | NamedIndividual |
| Robert_Glen_Coe | label | "Robert Glen Coe" |

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
