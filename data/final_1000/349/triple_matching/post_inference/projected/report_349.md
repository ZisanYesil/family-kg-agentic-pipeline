# Triple matching report: 349

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Silversun_Pickups | hasCountry | American |
| Silversun_Pickups | type | Artifact |
| Wampire | hasCountry | American |
| Wampire | type | Artifact |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| silversun_pickups_band | hasCountry | American |
| silversun_pickups_band | type | Agent |
| silversun_pickups_band | type | Organization |
| wampire_band | hasCountry | American |
| wampire_band | type | Agent |
| wampire_band | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 1 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.250000 |
| Recall | 0.333333 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
