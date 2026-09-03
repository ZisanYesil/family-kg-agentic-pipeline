# Triple matching report: 688

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Como_yo_te_quería | hasPublicationDate | "1944"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Sex_Is_Zero_2 | hasPublicationDate | "2007"^^<http://www.w3.org/2001/XMLSchema#gYear> |

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
| Como_yo_te_quería | type | Film |
| Como_yo_te_quería | type | NamedIndividual |
| Como_yo_te_quería | label | "Como yo te quería" |
| Sex_Is_Zero_2 | type | Film |
| Sex_Is_Zero_2 | type | NamedIndividual |
| Sex_Is_Zero_2 | label | "Sex Is Zero 2" |

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
