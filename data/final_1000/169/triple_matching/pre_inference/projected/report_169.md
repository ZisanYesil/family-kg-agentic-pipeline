# Triple matching report: 169

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Catherine_Charlotte_de_Gramont | hasDeathDate | "1678-06-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| Louis_I_Prince_of_Monaco | hasSpouse | Catherine_Charlotte_de_Gramont |

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
| Catherine_Charlotte_de_Gramont | type | Person |
| Catherine_Charlotte_de_Gramont | type | NamedIndividual |
| Catherine_Charlotte_de_Gramont | label | "Catherine Charlotte de Gramont" |
| Louis_I_Prince_of_Monaco | type | Person |
| Louis_I_Prince_of_Monaco | type | NamedIndividual |
| Louis_I_Prince_of_Monaco | label | "Louis I, Prince of Monaco" |

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
