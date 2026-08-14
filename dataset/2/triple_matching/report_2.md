# Triple matching report: 2

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Charge It to Me | type | Artifact |
| Charge It to Me | type | CreativeWork |
| Danger: Diabolik | type | Artifact |
| Danger: Diabolik | type | CreativeWork |
| Mario Bava | hasBirthDate | "1914-07-31"^^<http://www.w3.org/2001/XMLSchema#date> |
| Mario Bava | type | Agent |
| Mario Bava | type | Person |
| Roy William Neill | hasBirthDate | "1887-09-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| Roy William Neill | type | Agent |
| Roy William Neill | type | Person |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Charge It to Me | hasCreator | Roy William Neill |
| Charge It to Me | hasDirector | Roy William Neill |
| Danger: Diabolik | hasCreator | Mario Bava |
| Danger: Diabolik | hasDirector | Mario Bava |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Charge It to Me | hasPublicationDate | "1919"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Charge It to Me | type | Film |
| Danger: Diabolik | hasPublicationDate | "1968"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Danger: Diabolik | type | Film |
| Mario Bava | hasDeathDate | "1980-04-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Roy William Neill | hasDeathDate | "1946-12-14"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 14 |
| Union triples in scope | 20 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.625000 |
| Recall | 0.714286 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
