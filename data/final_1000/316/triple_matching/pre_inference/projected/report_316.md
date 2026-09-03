# Triple matching report: 316

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Hollywood_Shuffle | hasPublicationDate | "1987"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Thelma_Louise | hasPublicationDate | "1991"^^<http://www.w3.org/2001/XMLSchema#gYear> |

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
| Hollywood_Shuffle | type | Film |
| Hollywood_Shuffle | type | NamedIndividual |
| Hollywood_Shuffle | label | "Hollywood Shuffle" |
| Hollywood_Shuffle | altLabel | "Hollywood Shuffle" |
| Thelma_Louise | type | Film |
| Thelma_Louise | type | NamedIndividual |
| Thelma_Louise | label | "Thelma & Louise" |
| Thelma_Louise | altLabel | "Thelma & Louise" |

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
