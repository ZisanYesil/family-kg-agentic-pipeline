# Triple matching report: 843

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| De_Dannan | type | Agent |
| De_Dannan | type | Organization |
| Frankie_Gavin | type | Agent |
| Frankie_Gavin | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| British | type | Country |
| British | type | Place |
| De_Dannan | hasMember | Frankie_Gavin |
| Frankie_Gavin | hasCountry | British |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| De_Dannan | hasCountry | ireland |
| De_Dannan | hasFounder | Frankie_Gavin |
| ireland | type | Country |
| ireland | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.500000 |
| Recall | 0.500000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
