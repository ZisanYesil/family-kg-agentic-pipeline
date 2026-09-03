# Triple matching report: 975

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Agnieszka_Holland | hasBirthDate | "1948-11-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Talking_Feet | hasDirector | John_Baxter |
| The_Third_Miracle | hasDirector | Agnieszka_Holland |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| John_Baxter_director | hasBirthDate | "1896-12-31"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Agnieszka_Holland | type | Person |
| Agnieszka_Holland | type | NamedIndividual |
| Agnieszka_Holland | label | "Agnieszka Holland" |
| John_Baxter | hasBirthDate | "1896-12-31"^^<http://www.w3.org/2001/XMLSchema#date> |
| John_Baxter | hasDeathDate | "1975-01-21"^^<http://www.w3.org/2001/XMLSchema#date> |
| John_Baxter | type | Person |
| John_Baxter | type | NamedIndividual |
| John_Baxter | label | "John Baxter" |
| Talking_Feet | type | Film |
| Talking_Feet | type | NamedIndividual |
| Talking_Feet | label | "Talking Feet" |
| The_Third_Miracle | type | Film |
| The_Third_Miracle | type | NamedIndividual |
| The_Third_Miracle | label | "The Third Miracle" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 18 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.176471 |
| Recall | 0.750000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
