# Triple matching report: 345

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Italian | type | Country |
| Italian | type | Place |
| Pleasure_1931_film | hasCountry | American |
| Pleasure_1931_film | type | Artifact |
| Ten_Thousand_Dollars_for_a_Massacre | hasCountry | Italian |
| Ten_Thousand_Dollars_for_a_Massacre | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Pleasure_1931_film | type | CreativeWork |
| Pleasure_1931_film | type | Film |
| Ten_Thousand_Dollars_for_a_Massacre | type | CreativeWork |
| Ten_Thousand_Dollars_for_a_Massacre | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 12 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.666667 |
| Recall | 1.000000 |
| F1 score | 0.800000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
