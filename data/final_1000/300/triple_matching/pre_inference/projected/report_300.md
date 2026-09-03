# Triple matching report: 300

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alex_P | hasBirthDate | "1979-12-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Fuego | hasComposer | Alex_P |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Alex_P | type | Person |
| Alex_P | type | NamedIndividual |
| Alex_P | label | "Alexander \"Alex P\" Papaconstantinou" |
| Alex_P | altLabel | "Alex P" |
| Fuego | type | MusicalWork |
| Fuego | type | NamedIndividual |
| Fuego | label | "Fuego (Eleni Foureira song)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
