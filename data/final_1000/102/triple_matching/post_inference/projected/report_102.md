# Triple matching report: 102

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Hurlingham_Reggae_Band | hasMember | Luca_Prodan |
| Hurlingham_Reggae_Band | type | Agent |
| Hurlingham_Reggae_Band | type | Organization |
| Italian_Scottish | type | Country |
| Italian_Scottish | type | Place |
| Luca_Prodan | hasCountry | Italian_Scottish |
| Luca_Prodan | type | Agent |
| Luca_Prodan | type | Person |

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
| Luca_Prodan | hasCountry | italy |
| italy | type | Country |
| italy | type | Place |

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
