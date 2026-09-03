# Triple matching report: 523

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gillam_Airport | hasCountry | Canada |
| St_François_Xavier_Airport | hasCountry | Canada |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Canada | type | Country |
| Canada | type | NamedIndividual |
| Canada | label | "Canada" |
| Canada | altLabel | "Canada" |
| Gillam_Airport | type | Place |
| Gillam_Airport | type | NamedIndividual |
| Gillam_Airport | label | "Gillam Airport" |
| St_François_Xavier_Airport | type | Place |
| St_François_Xavier_Airport | type | NamedIndividual |
| St_François_Xavier_Airport | label | "St. François Xavier Airport" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
