# Triple matching report: 701

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Nubes_de_humo | hasPublicationDate | "1958"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| The_Samurai_in_Autumn | hasPublicationDate | "2016"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Nubes_de_humo | type | Film |
| Nubes_de_humo | type | NamedIndividual |
| Nubes_de_humo | label | "Nubes de humo" |
| Nubes_de_humo | altLabel | "Nubes de humo" |
| The_Samurai_in_Autumn | type | Film |
| The_Samurai_in_Autumn | type | NamedIndividual |
| The_Samurai_in_Autumn | label | "The Samurai in Autumn" |
| The_Samurai_in_Autumn | altLabel | "The Samurai in Autumn" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
