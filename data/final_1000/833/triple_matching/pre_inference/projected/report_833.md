# Triple matching report: 833

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Eager_Bodies | hasPublicationDate | "2003"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| We_Dive_at_Dawn | hasPublicationDate | "1943"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Eager_Bodies | type | Film |
| Eager_Bodies | type | NamedIndividual |
| Eager_Bodies | label | "Eager Bodies" |
| We_Dive_at_Dawn | type | Film |
| We_Dive_at_Dawn | type | NamedIndividual |
| We_Dive_at_Dawn | label | "We Dive at Dawn" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 8 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
