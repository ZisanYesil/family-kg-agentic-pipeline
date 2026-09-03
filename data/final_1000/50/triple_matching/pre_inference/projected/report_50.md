# Triple matching report: 50

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| A_Soldier_s_Oath | hasProducer | William_Fox |
| Nat_Cohen | hasDeathDate | "1988-02-10"^^<http://www.w3.org/2001/XMLSchema#date> |
| The_Criminal_1960_film | hasProducer | Nat_Cohen |

# 2. Unmatched triples

**Total unmatched count: 19**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| William_Fox_producer | hasDeathDate | "1952-05-08"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 18**

| Subject | Predicate | Object |
|---|---|---|
| A_Soldier_s_Oath | type | Film |
| A_Soldier_s_Oath | type | NamedIndividual |
| A_Soldier_s_Oath | label | "A Soldier's Oath" |
| Nat_Cohen | hasBirthDate | "1905-12-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Nat_Cohen | type | Person |
| Nat_Cohen | type | NamedIndividual |
| Nat_Cohen | label | "Nat Cohen" |
| The_Criminal_1960_film | type | Film |
| The_Criminal_1960_film | type | NamedIndividual |
| The_Criminal_1960_film | label | "The Criminal" |
| The_Criminal_1960_film | altLabel | "The Criminal (1960 film)" |
| William_Fox | hasBirthDate | "1879-01-01"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Fox | hasDeathDate | "1952-05-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Fox | type | Person |
| William_Fox | type | NamedIndividual |
| William_Fox | label | "William Fox" |
| William_Fox | altLabel | "Vilmos Fuchs" |
| William_Fox | altLabel | "William Fox" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 21 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 22 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 18 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.142857 |
| Recall | 0.750000 |
| F1 score | 0.240000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
