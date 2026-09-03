# Triple matching report: 774

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Go_for_Sisters | hasPublicationDate | "2013"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Jive_Junction | hasPublicationDate | "1943"^^<http://www.w3.org/2001/XMLSchema#gYear> |

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
| Go_for_Sisters | type | Film |
| Go_for_Sisters | type | NamedIndividual |
| Go_for_Sisters | label | "Go for Sisters" |
| Jive_Junction | type | Film |
| Jive_Junction | type | NamedIndividual |
| Jive_Junction | label | "Jive Junction" |

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
