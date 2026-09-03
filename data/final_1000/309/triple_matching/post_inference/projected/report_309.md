# Triple matching report: 309

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Charlemagne | hasSpouse | Luitgard |
| Charlemagne | type | Agent |
| Charlemagne | type | Person |
| Luitgard | hasSpouse | Charlemagne |
| Luitgard | type | Agent |
| Luitgard | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Carolingian_Empire | type | Country |
| Carolingian_Empire | type | Place |
| Charlemagne | hasCountry | Carolingian_Empire |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Charlemagne | hasCountry | frankish_country |
| frankish_country | type | Country |
| frankish_country | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 12 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.666667 |
| Recall | 0.666667 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
