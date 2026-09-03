# Triple matching report: 568

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Lucknow_Airpark | hasCountry | Canada |
| Valleyview_Airport | hasCountry | Canada |

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
| Canada | type | Country |
| Canada | type | NamedIndividual |
| Canada | label | "Canada" |
| Lucknow_Airpark | type | Artifact |
| Lucknow_Airpark | type | NamedIndividual |
| Lucknow_Airpark | label | "Lucknow Airpark" |
| Valleyview_Airport | type | Artifact |
| Valleyview_Airport | type | NamedIndividual |
| Valleyview_Airport | label | "Valleyview Airport" |

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
