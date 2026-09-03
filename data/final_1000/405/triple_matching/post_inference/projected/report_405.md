# Triple matching report: 405

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Dave_Bird | type | Agent |
| Dave_Bird | type | Person |
| Junkin_with_Val_and_Dave | hasCreator | Dave_Bird |
| Junkin_with_Val_and_Dave | type | Artifact |
| Junkin_with_Val_and_Dave | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Dave_Bird | hasBirthPlace | Gloucester |
| Gloucester | type | Place |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 5 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 7 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 2 |
| Precision | 1.000000 |
| Recall | 0.714286 |
| F1 score | 0.833333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
