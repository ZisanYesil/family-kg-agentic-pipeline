# Triple matching report: 887

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Franz_Antel | type | Agent |
| Franz_Antel | type | Person |
| No_Sin_on_the_Alpine_Pastures | hasCreator | Franz_Antel |
| No_Sin_on_the_Alpine_Pastures | hasDirector | Franz_Antel |
| No_Sin_on_the_Alpine_Pastures | type | Artifact |
| No_Sin_on_the_Alpine_Pastures | type | CreativeWork |
| No_Sin_on_the_Alpine_Pastures | type | Film |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Franz_Antel | hasDeathPlace | Vienna |
| Vienna | type | Place |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 9 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 2 |
| Precision | 1.000000 |
| Recall | 0.777778 |
| F1 score | 0.875000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
