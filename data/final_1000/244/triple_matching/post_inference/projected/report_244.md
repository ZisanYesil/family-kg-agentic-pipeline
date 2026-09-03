# Triple matching report: 244

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Forget_About_the_World | hasCreator | Gabrielle |
| Forget_About_the_World | hasPerformer | Gabrielle |
| Forget_About_the_World | type | Artifact |
| Forget_About_the_World | type | CreativeWork |
| Gabrielle | hasBirthPlace | Hackney |
| Gabrielle | type | Agent |
| Gabrielle | type | Person |
| Hackney | type | Place |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Forget_About_the_World | type | MusicalWork |
| Gabrielle | hasBirthDate | "1969-07-19"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 10 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.800000 |
| Recall | 1.000000 |
| F1 score | 0.888889 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
