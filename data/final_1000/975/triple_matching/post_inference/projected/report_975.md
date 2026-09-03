# Triple matching report: 975

# 1. Matched triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Agnieszka_Holland | hasBirthDate | "1948-11-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Agnieszka_Holland | type | Agent |
| Agnieszka_Holland | type | Person |
| John_Baxter | type | Agent |
| John_Baxter | type | Person |
| Talking_Feet | hasCreator | John_Baxter |
| Talking_Feet | hasDirector | John_Baxter |
| Talking_Feet | type | Artifact |
| Talking_Feet | type | CreativeWork |
| Talking_Feet | type | Film |
| The_Third_Miracle | hasCreator | Agnieszka_Holland |
| The_Third_Miracle | hasDirector | Agnieszka_Holland |
| The_Third_Miracle | type | Artifact |
| The_Third_Miracle | type | CreativeWork |
| The_Third_Miracle | type | Film |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| John_Baxter_director | hasBirthDate | "1896-12-31"^^<http://www.w3.org/2001/XMLSchema#date> |
| John_Baxter_director | type | Agent |
| John_Baxter_director | type | Person |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| John_Baxter | hasBirthDate | "1896-12-31"^^<http://www.w3.org/2001/XMLSchema#date> |
| John_Baxter | hasDeathDate | "1975-01-21"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 18 |
| Union triples in scope | 20 |
| True positives (matched) | 15 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.882353 |
| Recall | 0.833333 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
