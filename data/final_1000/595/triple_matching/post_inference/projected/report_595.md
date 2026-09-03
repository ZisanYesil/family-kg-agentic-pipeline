# Triple matching report: 595

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Australian | type | Country |
| Australian | type | Place |
| Gordon_Elliott | hasCountry | Australian |
| Gordon_Elliott | type | Agent |
| Gordon_Elliott | type | Person |
| Road_Tasted | hasCreator | Gordon_Elliott |
| Road_Tasted | type | Artifact |
| Road_Tasted | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Gordon_Elliott | hasCountry | united_kingdom |
| united_kingdom | type | Country |
| united_kingdom | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 11 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.727273 |
| Recall | 1.000000 |
| F1 score | 0.842105 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
