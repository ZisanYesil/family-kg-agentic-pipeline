# Triple matching report: 194

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Inside_My_Love | hasCreator | Minnie_Riperton |
| Inside_My_Love | hasPerformer | Minnie_Riperton |
| Inside_My_Love | type | Artifact |
| Inside_My_Love | type | CreativeWork |
| Minnie_Riperton | type | Agent |
| Minnie_Riperton | type | Person |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Chicago | type | Place |
| Minnie_Riperton | hasBirthPlace | Chicago |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 2 |
| Precision | 1.000000 |
| Recall | 0.750000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
