# Triple matching report: 369

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Pye_Min | hasParent | Thalun |
| Pye_Min | type | Agent |
| Pye_Min | type | Person |
| Thalun | hasChild | Pye_Min |
| Thalun | type | Agent |
| Thalun | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Anaukpetlun | hasSibling | Thalun |
| Anaukpetlun | type | Agent |
| Anaukpetlun | type | Person |
| Thalun | hasSibling | Anaukpetlun |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Thalun | hasSibling | minye_kyawswa_ii |
| minye_kyawswa_ii | hasSibling | Thalun |
| minye_kyawswa_ii | type | Agent |
| minye_kyawswa_ii | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 14 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.600000 |
| Recall | 0.600000 |
| F1 score | 0.600000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
