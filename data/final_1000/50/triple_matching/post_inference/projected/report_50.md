# Triple matching report: 50

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| A_Soldier_s_Oath | hasProducer | William_Fox |
| A_Soldier_s_Oath | type | Artifact |
| A_Soldier_s_Oath | type | CreativeWork |
| Nat_Cohen | hasDeathDate | "1988-02-10"^^<http://www.w3.org/2001/XMLSchema#date> |
| Nat_Cohen | type | Agent |
| Nat_Cohen | type | Person |
| The_Criminal_1960_film | hasProducer | Nat_Cohen |
| The_Criminal_1960_film | type | Artifact |
| The_Criminal_1960_film | type | CreativeWork |
| William_Fox | type | Agent |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| William_Fox_producer | hasDeathDate | "1952-05-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Fox_producer | type | Agent |
| William_Fox_producer | type | Person |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| A_Soldier_s_Oath | type | Film |
| Nat_Cohen | hasBirthDate | "1905-12-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| The_Criminal_1960_film | type | Film |
| William_Fox | hasBirthDate | "1879-01-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Fox | hasDeathDate | "1952-05-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Fox | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 13 |
| Union triples in scope | 19 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.625000 |
| Recall | 0.769231 |
| F1 score | 0.689655 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
