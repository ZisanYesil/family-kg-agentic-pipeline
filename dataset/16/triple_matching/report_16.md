# Triple matching report: 16

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Q17353699 | hasBirthDate | "1919-11-28"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q17353699 | type | Agent |
| Q17353699 | type | Person |
| Q21869977 | hasCreator | Q17353699 |
| Q21869977 | hasDirector | Q17353699 |
| Q21869977 | type | Artifact |
| Q21869977 | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Q17353699 | hasDeathDate | "2014-07-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q21869977 | hasPublicationDate | "1925"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q21869977 | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 10 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.700000 |
| Recall | 1.000000 |
| F1 score | 0.823529 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
