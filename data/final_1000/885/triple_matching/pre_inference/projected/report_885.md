# Triple matching report: 885

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Ståle_Storløkken | hasBirthPlace | Dombås_Norway |
| Veslefrekk | hasMember | Ståle_Storløkken |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Dombås_Norway | type | Place |
| Dombås_Norway | type | NamedIndividual |
| Dombås_Norway | label | "Dombås, Norway" |
| Dombås_Norway | altLabel | "Dombås" |
| Ståle_Storløkken | type | Person |
| Ståle_Storløkken | type | NamedIndividual |
| Ståle_Storløkken | label | "Ståle Storløkken" |
| Veslefrekk | type | Organization |
| Veslefrekk | type | NamedIndividual |
| Veslefrekk | label | "Veslefrekk" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
