# Triple matching report: 776

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| British | type | Country |
| British | type | Place |
| Nancy_Drew_Trouble_Shooter | hasCountry | American |
| Nancy_Drew_Trouble_Shooter | type | Artifact |
| Wilderness_miniseries | hasCountry | British |
| Wilderness_miniseries | type | Artifact |

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
| Nancy_Drew_Trouble_Shooter | type | CreativeWork |
| Nancy_Drew_Trouble_Shooter | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 10 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.800000 |
| Recall | 1.000000 |
| F1 score | 0.888889 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
