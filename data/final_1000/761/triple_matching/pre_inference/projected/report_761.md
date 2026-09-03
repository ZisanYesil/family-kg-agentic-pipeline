# Triple matching report: 761

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Sammy_Drechsel | hasBirthDate | "1925-04-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sammy_Drechsel | hasDeathDate | "1986-01-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Wolfgang_Fischer | hasBirthDate | "1888-12-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Wolfgang_Fischer | hasDeathDate | "1943-02-01"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Sammy_Drechsel | type | Person |
| Sammy_Drechsel | type | NamedIndividual |
| Sammy_Drechsel | label | "Sammy Drechsel" |
| Sammy_Drechsel | altLabel | "Karl- Heinz Kamke" |
| Wolfgang_Fischer | type | Person |
| Wolfgang_Fischer | type | NamedIndividual |
| Wolfgang_Fischer | label | "Wolfgang Fischer" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 11 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.363636 |
| Recall | 1.000000 |
| F1 score | 0.533333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
