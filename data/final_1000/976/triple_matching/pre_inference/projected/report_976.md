# Triple matching report: 976

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Charles_Prince_of_Nassau_Usingen | hasBirthDate | "1712-12-31"^^<http://www.w3.org/2001/XMLSchema#date> |
| Charles_Émile_Troisier | hasBirthDate | "1844-04-06"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Charles_Prince_of_Nassau_Usingen | type | Person |
| Charles_Prince_of_Nassau_Usingen | type | NamedIndividual |
| Charles_Prince_of_Nassau_Usingen | label | "Charles, Prince of Nassau-Usingen" |
| Charles_Émile_Troisier | type | Person |
| Charles_Émile_Troisier | type | NamedIndividual |
| Charles_Émile_Troisier | label | "Charles Émile Troisier" |

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
