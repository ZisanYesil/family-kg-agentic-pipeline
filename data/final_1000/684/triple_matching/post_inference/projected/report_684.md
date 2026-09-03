# Triple matching report: 684

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Bona_Sforza | hasChild | Sigismund_II_Augustus |
| Bona_Sforza | type | Agent |
| Bona_Sforza | type | Person |
| Sigismund_II_Augustus | hasParent | Bona_Sforza |
| Sigismund_II_Augustus | type | Agent |
| Sigismund_II_Augustus | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Bona_Sforza | hasCountry | Duchy_of_Milan |
| Duchy_of_Milan | type | Country |
| Duchy_of_Milan | type | Place |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Bona_Sforza | hasCountry | italy |
| italy | type | Country |
| italy | type | Place |

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
