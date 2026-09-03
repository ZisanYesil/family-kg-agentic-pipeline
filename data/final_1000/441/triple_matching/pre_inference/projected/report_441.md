# Triple matching report: 441

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Olivier_Long | hasBirthDate | "1915-10-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Olivier_Long | hasDeathDate | "2003-03-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Robert_Ernest_Cheesman | hasBirthDate | "1878"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Robert_Ernest_Cheesman | hasDeathDate | "1962-02-13"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Olivier_Long | type | Person |
| Olivier_Long | type | NamedIndividual |
| Olivier_Long | label | "Olivier Long" |
| Robert_Ernest_Cheesman | type | Person |
| Robert_Ernest_Cheesman | type | NamedIndividual |
| Robert_Ernest_Cheesman | label | "Robert Ernest Cheesman" |

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
