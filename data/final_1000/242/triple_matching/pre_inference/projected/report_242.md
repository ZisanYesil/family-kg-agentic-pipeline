# Triple matching report: 242

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Chester_Ray_Benjamin | hasBirthDate | "1923-01-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Chester_Ray_Benjamin | hasDeathDate | "2002-04-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ernest_Duff | hasBirthDate | "1931-06-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ernest_Duff | hasDeathDate | "2016-05-27"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Chester_Ray_Benjamin | type | Person |
| Chester_Ray_Benjamin | type | NamedIndividual |
| Chester_Ray_Benjamin | label | "Chester Ray Benjamin" |
| Ernest_Duff | type | Person |
| Ernest_Duff | type | NamedIndividual |
| Ernest_Duff | label | "Ernest Duff" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 10 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.400000 |
| Recall | 1.000000 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
