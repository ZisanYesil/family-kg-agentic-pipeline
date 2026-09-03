# Triple matching report: 445

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Hollywood_California | type | Place |
| Marvin_Hatley | hasDeathPlace | Hollywood_California |
| Marvin_Hatley | type | Agent |
| Marvin_Hatley | type | Person |
| There_Goes_My_Heart | hasComposer | Marvin_Hatley |
| There_Goes_My_Heart | hasCreator | Marvin_Hatley |
| There_Goes_My_Heart | type | Artifact |
| There_Goes_My_Heart | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| There_Goes_My_Heart | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 9 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.888889 |
| Recall | 1.000000 |
| F1 score | 0.941176 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
