# Triple matching report: 46

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| British | type | Country |
| British | type | Place |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Freestylers | hasCountry | British |
| Freestylers | type | Artifact |
| The_Nouvelles | hasCountry | British |
| The_Nouvelles | type | Artifact |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| freestylers | hasCountry | British |
| freestylers | type | Agent |
| freestylers | type | Organization |
| the_nouvelles | hasCountry | British |
| the_nouvelles | type | Agent |
| the_nouvelles | type | Organization |

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
