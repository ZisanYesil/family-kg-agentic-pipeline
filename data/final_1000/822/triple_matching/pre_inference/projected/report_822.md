# Triple matching report: 822

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Ang_Nan | hasDeathPlace | Srey_Santhor |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Ang_Em | hasParent | Ang_Nan |

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Ang_Em | hasBirthDate | "1674-01-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ang_Em | hasDeathDate | "1731-01-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ang_Em | type | Person |
| Ang_Em | type | NamedIndividual |
| Ang_Em | label | "Ang Em" |
| Ang_Em | altLabel | "Barom Reameathiptei" |
| Ang_Nan | hasBirthDate | "1654-01-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ang_Nan | hasChild | Ang_Em |
| Ang_Nan | hasDeathDate | "1691-01-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ang_Nan | type | Person |
| Ang_Nan | type | NamedIndividual |
| Ang_Nan | label | "Ang Nan" |
| Srey_Santhor | type | Place |
| Srey_Santhor | type | NamedIndividual |
| Srey_Santhor | label | "Srey Santhor" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 17 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.062500 |
| Recall | 0.500000 |
| F1 score | 0.111111 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
