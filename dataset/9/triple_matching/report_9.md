# Triple matching report: 9

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Q220 | type | Place |
| Q232190 | type | Artifact |
| Q232190 | type | CreativeWork |
| Q697834 | hasBirthPlace | Q220 |
| Q697834 | type | Agent |
| Q697834 | type | Person |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Q232190 | hasCreator | Q697834 |
| Q232190 | hasDirector | Q697834 |

## 2.2 Extracted-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Q220 | type | GeographicLocation |
| Q232190 | hasPublicationDate | "1961"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q232190 | type | Film |
| Q697834 | hasBirthDate | "1922-09-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q697834 | hasDeathDate | "1989-12-17"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 13 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 5 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.545455 |
| Recall | 0.750000 |
| F1 score | 0.631579 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
