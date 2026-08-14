# Triple matching report: 13

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Q16 | type | Country |
| Q16 | type | Place |
| Q633 | hasCitizenship | Q16 |
| Q633 | hasCountry | Q16 |
| Q633 | type | Agent |
| Q633 | type | Person |
| Q7557270 | type | Artifact |
| Q7557270 | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Q7557270 | hasCreator | Q633 |
| Q7557270 | hasPerformer | Q633 |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Q633 | hasBirthDate | "1945-11-12"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q7557270 | hasPublicationDate | "1972"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q7557270 | type | MusicalWork |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 13 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.727273 |
| Recall | 0.800000 |
| F1 score | 0.761905 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
