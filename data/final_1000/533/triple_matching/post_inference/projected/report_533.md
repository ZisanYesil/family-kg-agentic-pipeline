# Triple matching report: 533

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Janine_Krieber | hasSpouse | Stéphane_Dion |
| Janine_Krieber | type | Agent |
| Janine_Krieber | type | Person |
| Stéphane_Dion | hasSpouse | Janine_Krieber |
| Stéphane_Dion | type | Agent |
| Stéphane_Dion | type | Person |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Stéphane_Dion | hasEmployer | Université_de_Montréal |
| Université_de_Montréal | type | Agent |
| Université_de_Montréal | type | Organization |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| germany | type | Country |
| germany | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 11 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.750000 |
| Recall | 0.666667 |
| F1 score | 0.705882 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
