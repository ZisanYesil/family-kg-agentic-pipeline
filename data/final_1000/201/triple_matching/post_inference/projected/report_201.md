# Triple matching report: 201

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| David_Ridgway | hasSpouse | Francesca_Romana_Serra_Ridgway |
| David_Ridgway | type | Agent |
| David_Ridgway | type | Person |
| Francesca_Romana_Serra_Ridgway | hasSpouse | David_Ridgway |
| Francesca_Romana_Serra_Ridgway | type | Agent |
| Francesca_Romana_Serra_Ridgway | type | Person |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Athens | type | Place |
| David_Ridgway | hasBirthPlace | Athens |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 2 |
| Precision | 1.000000 |
| Recall | 0.750000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
