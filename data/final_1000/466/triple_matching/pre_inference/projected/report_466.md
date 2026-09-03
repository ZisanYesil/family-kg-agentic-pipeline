# Triple matching report: 466

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| J_M_Balliol_Salmon | hasBirthDate | "1868"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| J_M_Balliol_Salmon | hasDeathDate | "1953"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Edward_Stillingfleet | hasBirthDate | "1635"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Edward_Stillingfleet | hasDeathDate | "1699"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Edward_Stillingfleet | hasBirthDate | "1660"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Edward_Stillingfleet | hasDeathDate | "1708"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Edward_Stillingfleet | type | Person |
| Edward_Stillingfleet | type | NamedIndividual |
| Edward_Stillingfleet | label | "Edward Stillingfleet" |
| J_M_Balliol_Salmon | type | Person |
| J_M_Balliol_Salmon | type | NamedIndividual |
| J_M_Balliol_Salmon | label | "J M Balliol Salmon" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.200000 |
| Recall | 0.500000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
