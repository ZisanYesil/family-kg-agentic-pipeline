# Triple matching report: 789

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Curly_Seckler | hasBirthDate | "1919-12-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Curly_Seckler | hasDeathDate | "2017-12-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| James_Flack_Norris | hasBirthDate | "1871-01-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| James_Flack_Norris | hasDeathDate | "1940"^^<http://www.w3.org/2001/XMLSchema#gYear> |

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
| Curly_Seckler | type | Person |
| Curly_Seckler | type | NamedIndividual |
| Curly_Seckler | label | "Curly Seckler" |
| Curly_Seckler | altLabel | "John Ray Sechler" |
| James_Flack_Norris | type | Person |
| James_Flack_Norris | type | NamedIndividual |
| James_Flack_Norris | label | "James Flack Norris" |

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
