# Triple matching report: 18

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Q3514179 | type | Artifact |
| Q3514179 | type | CreativeWork |
| Q358322 | hasBirthDate | "1912-10-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q358322 | type | Agent |
| Q358322 | type | Person |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Q3514179 | hasCreator | Q358322 |
| Q3514179 | hasDirector | Q358322 |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Q3514179 | hasPublicationDate | "1954"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q3514179 | type | Film |
| Q358322 | hasDeathDate | "1991-04-20"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 10 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.625000 |
| Recall | 0.714286 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
