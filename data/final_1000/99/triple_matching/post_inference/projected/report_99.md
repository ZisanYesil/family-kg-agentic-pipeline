# Triple matching report: 99

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Blácaire_mac_Gofraid | type | Agent |
| Blácaire_mac_Gofraid | type | Person |
| Gofraid_ua_Ímair | hasChild | Olaf_Guthfrithson |
| Gofraid_ua_Ímair | type | Agent |
| Gofraid_ua_Ímair | type | Person |
| Olaf_Guthfrithson | hasParent | Gofraid_ua_Ímair |
| Olaf_Guthfrithson | type | Agent |
| Olaf_Guthfrithson | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Amlaíb_mac_Gofraid | hasSibling | Blácaire_mac_Gofraid |
| Amlaíb_mac_Gofraid | type | Agent |
| Amlaíb_mac_Gofraid | type | Person |
| Blácaire_mac_Gofraid | hasSibling | Amlaíb_mac_Gofraid |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Blácaire_mac_Gofraid | hasSibling | Olaf_Guthfrithson |
| Olaf_Guthfrithson | hasSibling | Blácaire_mac_Gofraid |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 14 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.800000 |
| Recall | 0.666667 |
| F1 score | 0.727273 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
