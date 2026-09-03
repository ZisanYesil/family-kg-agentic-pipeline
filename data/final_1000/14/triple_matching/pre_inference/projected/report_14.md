# Triple matching report: 14

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Old_Man_Drinking_a_Glass_of_Beer | hasDirector | George_Albert_Smith |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| George_Albert_Smith | hasDeathPlace | Brighton |

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| George_Albert_Smith | hasBirthDate | "1864-01-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| George_Albert_Smith | hasDeathDate | "1959-05-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| George_Albert_Smith | type | Person |
| George_Albert_Smith | type | NamedIndividual |
| George_Albert_Smith | label | "George Albert Smith" |
| Old_Man_Drinking_a_Glass_of_Beer | type | Film |
| Old_Man_Drinking_a_Glass_of_Beer | type | NamedIndividual |
| Old_Man_Drinking_a_Glass_of_Beer | label | "Old Man Drinking a Glass of Beer" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.111111 |
| Recall | 0.500000 |
| F1 score | 0.181818 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
