# Triple matching report: 961

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Adam_Carolla | hasBirthDate | "1964-05-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Justin_Edgar | hasBirthDate | "1971-08-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Road_Hard | hasDirector | Adam_Carolla |
| We_Are_the_Freaks | hasDirector | Justin_Edgar |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Adam_Carolla | type | Person |
| Adam_Carolla | type | NamedIndividual |
| Adam_Carolla | label | "Adam Carolla" |
| Justin_Edgar | type | Person |
| Justin_Edgar | type | NamedIndividual |
| Justin_Edgar | label | "Justin Edgar" |
| Road_Hard | type | Film |
| Road_Hard | type | NamedIndividual |
| Road_Hard | label | "Road Hard" |
| We_Are_the_Freaks | type | Film |
| We_Are_the_Freaks | type | NamedIndividual |
| We_Are_the_Freaks | label | "We Are the Freaks" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 16 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
