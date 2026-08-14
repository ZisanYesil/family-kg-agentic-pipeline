# Triple matching report: 7

# 1. Matched triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Q183 | type | Country |
| Q183 | type | Place |
| Q2707484 | type | Artifact |
| Q2707484 | type | CreativeWork |
| Q30 | type | Country |
| Q30 | type | Place |
| Q387784 | type | Artifact |
| Q387784 | type | CreativeWork |
| Q773242 | hasCitizenship | Q30 |
| Q773242 | hasCountry | Q30 |
| Q773242 | type | Agent |
| Q773242 | type | Person |
| Q97799 | hasCitizenship | Q183 |
| Q97799 | hasCountry | Q183 |
| Q97799 | type | Agent |
| Q97799 | type | Person |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Q2707484 | hasCreator | Q773242 |
| Q2707484 | hasDirector | Q773242 |
| Q387784 | hasCreator | Q97799 |
| Q387784 | hasDirector | Q97799 |

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Q2707484 | hasPublicationDate | "1936"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q2707484 | type | Film |
| Q387784 | hasPublicationDate | "1958"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q387784 | type | Film |
| Q773242 | hasBirthDate | "1895-11-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q773242 | hasDeathDate | "1936-07-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Q97799 | hasBirthDate | "1909"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q97799 | hasDeathDate | "1999"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 6 |
| Extracted triples in scope | 24 |
| Ground-truth triples in scope | 20 |
| Union triples in scope | 28 |
| True positives (matched) | 16 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.666667 |
| Recall | 0.800000 |
| F1 score | 0.727273 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
