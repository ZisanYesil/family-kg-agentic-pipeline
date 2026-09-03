# Triple matching report: 833

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Eager_Bodies | hasPublicationDate | "2003"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Eager_Bodies | type | Artifact |
| Eager_Bodies | type | CreativeWork |
| We_Dive_at_Dawn | hasPublicationDate | "1943"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| We_Dive_at_Dawn | type | Artifact |
| We_Dive_at_Dawn | type | CreativeWork |

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
| Eager_Bodies | type | Film |
| We_Dive_at_Dawn | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.750000 |
| Recall | 1.000000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
