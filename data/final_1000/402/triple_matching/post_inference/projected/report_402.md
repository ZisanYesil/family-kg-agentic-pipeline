# Triple matching report: 402

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Basilica_of_St_Lucia_Timotes | hasCountry | Venezuela |
| Saint_Augustine_by_the_Sea_Catholic_Church | hasCountry | United_States |
| United_States | type | Country |
| United_States | type | Place |
| Venezuela | type | Country |
| Venezuela | type | Place |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Basilica_of_St_Lucia_Timotes | type | Artifact |
| Saint_Augustine_by_the_Sea_Catholic_Church | type | Artifact |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.750000 |
| Recall | 1.000000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
