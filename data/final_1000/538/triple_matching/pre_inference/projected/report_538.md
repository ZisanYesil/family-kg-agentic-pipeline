# Triple matching report: 538

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Herbert_Wise | hasChild | Susannah_Wise |
| Reunion_at_Fairborough | hasDirector | Herbert_Wise |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Herbert_Wise | hasChild | charlie_walker_wise |
| Herbert_Wise | type | Person |
| Herbert_Wise | type | NamedIndividual |
| Herbert_Wise | label | "Herbert Wise" |
| Reunion_at_Fairborough | type | Film |
| Reunion_at_Fairborough | type | NamedIndividual |
| Reunion_at_Fairborough | label | "Reunion at Fairborough" |
| Susannah_Wise | type | Person |
| Susannah_Wise | type | NamedIndividual |
| Susannah_Wise | label | "Susannah Wise" |
| charlie_walker_wise | type | Person |
| charlie_walker_wise | type | NamedIndividual |
| charlie_walker_wise | label | "Charlie Walker-Wise" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
