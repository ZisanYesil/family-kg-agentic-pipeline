# Triple matching report: 264

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Buckaroo | hasPerformer | Lee_Ann_Womack |
| Lee_Ann_Womack | hasChild | Aubrie_Sellers |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Aubrie_Sellers | type | Person |
| Aubrie_Sellers | type | NamedIndividual |
| Aubrie_Sellers | label | "Aubrie Sellers" |
| Buckaroo | type | MusicalWork |
| Buckaroo | type | NamedIndividual |
| Buckaroo | label | "Buckaroo" |
| Lee_Ann_Womack | type | Person |
| Lee_Ann_Womack | type | NamedIndividual |
| Lee_Ann_Womack | label | "Lee Ann Womack" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
