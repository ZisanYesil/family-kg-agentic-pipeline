# Triple matching report: 921

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| K_9_P_I | hasDirector | Richard_J_Lewis |
| Richard_J_Lewis | hasBirthPlace | Toronto_Ontario |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| K_9_P_I | type | Film |
| K_9_P_I | type | NamedIndividual |
| K_9_P_I | label | "K-9: P.I." |
| Richard_J_Lewis | type | Person |
| Richard_J_Lewis | type | NamedIndividual |
| Richard_J_Lewis | label | "Richard J. Lewis" |
| Toronto_Ontario | type | Place |
| Toronto_Ontario | type | NamedIndividual |
| Toronto_Ontario | label | "Toronto, Ontario, Canada" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
