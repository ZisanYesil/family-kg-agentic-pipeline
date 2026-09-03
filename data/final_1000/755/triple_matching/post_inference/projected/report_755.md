# Triple matching report: 755

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Before_the_Streets | hasCountry | Canadian |
| Before_the_Streets | type | Artifact |
| Buchanan_Rides_Alone | hasCountry | American |
| Buchanan_Rides_Alone | type | Artifact |
| Canadian | type | Country |
| Canadian | type | Place |

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
| Before_the_Streets | type | CreativeWork |
| Before_the_Streets | type | Film |
| Buchanan_Rides_Alone | type | CreativeWork |
| Buchanan_Rides_Alone | type | Film |

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
