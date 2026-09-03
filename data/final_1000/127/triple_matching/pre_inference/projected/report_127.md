# Triple matching report: 127

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Chuck_Berry | hasBirthPlace | St_Louis_Missouri |
| Wee_Wee_Hours | hasPerformer | Chuck_Berry |

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
| Chuck_Berry | type | Person |
| Chuck_Berry | type | NamedIndividual |
| Chuck_Berry | label | "Chuck Berry" |
| St_Louis_Missouri | type | Place |
| St_Louis_Missouri | type | NamedIndividual |
| St_Louis_Missouri | label | "St. Louis, Missouri" |
| Wee_Wee_Hours | type | CreativeWork |
| Wee_Wee_Hours | type | NamedIndividual |
| Wee_Wee_Hours | label | "Wee Wee Hours" |

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
