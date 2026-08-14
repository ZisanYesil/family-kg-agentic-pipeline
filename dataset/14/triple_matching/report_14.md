# Triple matching report: 14

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Q4764595 | type | Agent |
| Q4764595 | type | Person |
| Q668 | type | Country |
| Q668 | type | Place |
| Q79781208 | type | Artifact |
| Q79781208 | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Q4764595 | hasCitizenship | Q668 |
| Q4764595 | hasCountry | Q668 |
| Q79781208 | hasCreator | Q4764595 |
| Q79781208 | hasDirector | Q4764595 |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Q79781208 | hasCountry | Q668 |
| Q79781208 | hasCountryOfOrigin | Q668 |
| Q79781208 | hasPublicationDate | "2019"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q79781208 | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 14 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.600000 |
| Recall | 0.600000 |
| F1 score | 0.600000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
