# Triple matching report: 374

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Julia_Bracken_Wendt | hasSpouse | William_Wendt |
| Julia_Bracken_Wendt | type | Agent |
| Julia_Bracken_Wendt | type | Person |
| William_Wendt | hasSpouse | Julia_Bracken_Wendt |
| William_Wendt | type | Agent |
| William_Wendt | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| German | type | Place |
| William_Wendt | hasBirthPlace | German |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| William_Wendt | hasBirthPlace | bentzen_kingdom_of_prussia |
| bentzen_kingdom_of_prussia | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 10 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.750000 |
| Recall | 0.750000 |
| F1 score | 0.750000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
