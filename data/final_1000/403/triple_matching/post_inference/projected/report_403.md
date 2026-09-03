# Triple matching report: 403

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Ash_Koosha | hasCountry | British_Iranian |
| Ash_Koosha | type | Agent |
| Ash_Koosha | type | Person |
| British_Iranian | type | Country |
| British_Iranian | type | Place |
| Take_It_Easy_Hospital | type | Agent |
| Take_It_Easy_Hospital | type | Organization |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Take_It_Easy_Hospital | hasMember | Ash_Koosha |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Ash_Koosha | hasCountry | united_kingdom |
| Take_It_Easy_Hospital | hasFounder | Ash_Koosha |
| united_kingdom | type | Country |
| united_kingdom | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 12 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.636364 |
| Recall | 0.875000 |
| F1 score | 0.736842 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
