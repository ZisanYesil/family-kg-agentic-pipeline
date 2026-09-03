# Triple matching report: 690

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Berkeley_in_the_Sixties | hasPublicationDate | "1990"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Caesar_Must_Die | hasPublicationDate | "2012"^^<http://www.w3.org/2001/XMLSchema#gYear> |

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
| Berkeley_in_the_Sixties | type | Film |
| Berkeley_in_the_Sixties | type | NamedIndividual |
| Berkeley_in_the_Sixties | label | "Berkeley in the Sixties" |
| Berkeley_in_the_Sixties | altLabel | "Berkeley in the Sixties" |
| Caesar_Must_Die | type | Film |
| Caesar_Must_Die | type | NamedIndividual |
| Caesar_Must_Die | label | "Caesar Must Die" |
| Caesar_Must_Die | altLabel | "Caesar Must Die" |

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
