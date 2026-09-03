# Triple matching report: 330

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Drogo_of_Champagne | type | Agent |
| Drogo_of_Champagne | type | Person |
| Pepin_of_Herstal | type | Agent |
| Pepin_of_Herstal | type | Person |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Drogo_of_Champagne | hasParent | Plectrudis |
| Pepin_of_Herstal | hasSpouse | Plectrude |
| Plectrude | hasSpouse | Pepin_of_Herstal |
| Plectrude | type | Agent |
| Plectrude | type | Person |
| Plectrudis | hasChild | Drogo_of_Champagne |
| Plectrudis | type | Agent |
| Plectrudis | type | Person |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Drogo_of_Champagne | hasChild | Pepin_of_Herstal |
| Pepin_of_Herstal | hasParent | Drogo_of_Champagne |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 14 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 8 |
| Precision | 0.666667 |
| Recall | 0.333333 |
| F1 score | 0.444444 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
