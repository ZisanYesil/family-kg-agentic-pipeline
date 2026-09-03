# Triple matching report: 998

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Finn_Jarle_Sæle | type | Agent |
| Finn_Jarle_Sæle | type | Person |
| Finn_Ørjan_Sæle | type | Agent |
| Finn_Ørjan_Sæle | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Anita_Apelthun_Sæle | hasChild | Finn_Ørjan_Sæle |
| Anita_Apelthun_Sæle | hasSpouse | Finn_Jarle_Sæle |
| Anita_Apelthun_Sæle | type | Agent |
| Anita_Apelthun_Sæle | type | Person |
| Finn_Jarle_Sæle | hasSpouse | Anita_Apelthun_Sæle |
| Finn_Ørjan_Sæle | hasParent | Anita_Apelthun_Sæle |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Finn_Jarle_Sæle | hasChild | Finn_Ørjan_Sæle |
| Finn_Ørjan_Sæle | hasParent | Finn_Jarle_Sæle |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.666667 |
| Recall | 0.400000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
