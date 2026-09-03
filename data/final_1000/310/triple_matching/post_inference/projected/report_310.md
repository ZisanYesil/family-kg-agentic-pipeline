# Triple matching report: 310

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Ramiro_I_of_Aragon | type | Agent |
| Ramiro_I_of_Aragon | type | Person |
| Sancho_Ramírez | type | Agent |
| Sancho_Ramírez | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Ermesinda_of_Bigorre | hasChild | Sancho_Ramírez |
| Ermesinda_of_Bigorre | hasSpouse | Ramiro_I_of_Aragon |
| Ermesinda_of_Bigorre | type | Agent |
| Ermesinda_of_Bigorre | type | Person |
| Ramiro_I_of_Aragon | hasSpouse | Ermesinda_of_Bigorre |
| Sancho_Ramírez | hasParent | Ermesinda_of_Bigorre |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Ramiro_I_of_Aragon | hasChild | Sancho_Ramírez |
| Sancho_Ramírez | hasParent | Ramiro_I_of_Aragon |

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
