# Triple matching report: 409

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Florence_of_Holland | type | Agent |
| Florence_of_Holland | type | Person |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Ada_of_Huntingdon | hasChild | Florence_of_Holland |
| Ada_of_Huntingdon | hasSpouse | Floris_III |
| Ada_of_Huntingdon | type | Agent |
| Ada_of_Huntingdon | type | Person |
| Florence_of_Holland | hasParent | Ada_of_Huntingdon |
| Floris_III | hasSpouse | Ada_of_Huntingdon |
| Floris_III | type | Agent |
| Floris_III | type | Person |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Florence_of_Holland | hasParent | florence_iii_count_of_holland |
| florence_iii_count_of_holland | hasChild | Florence_of_Holland |
| florence_iii_count_of_holland | type | Agent |
| florence_iii_count_of_holland | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 1 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 8 |
| Precision | 0.333333 |
| Recall | 0.200000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
