# Triple matching report: 610

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Cuatro | hasDirector | Tim_Wheeler |
| Tim_Wheeler | hasCountry | Northern_Irish |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Cuatro | type | Film |
| Cuatro | type | NamedIndividual |
| Cuatro | label | "¡Cuatro!" |
| Northern_Irish | type | Country |
| Northern_Irish | type | NamedIndividual |
| Northern_Irish | label | "United Kingdom" |
| Northern_Irish | altLabel | "Northern Irish" |
| Tim_Wheeler | type | Person |
| Tim_Wheeler | type | NamedIndividual |
| Tim_Wheeler | label | "Tim Wheeler" |
| Tim_Wheeler | altLabel | "Timothy James Arthur Wheeler" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
