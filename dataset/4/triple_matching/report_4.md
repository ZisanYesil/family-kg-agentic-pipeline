# Triple matching report: 4

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Q176135 | type | Artifact |
| Q176135 | type | CreativeWork |
| Q40646 | type | Agent |
| Q40646 | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Q176135 | hasCreator | Q40646 |
| Q176135 | hasDirector | Q40646 |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Q176135 | hasPublicationDate | "1950"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q176135 | type | Film |
| Q40646 | hasBirthDate | "1897-12-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q40646 | hasDeathDate | "1961-08-10"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 10 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.500000 |
| Recall | 0.666667 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
