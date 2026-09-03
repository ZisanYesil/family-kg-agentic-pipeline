# Triple matching report: 886

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Æthelred_died_after_704_was_King_of_Mercia | type | Agent |
| Æthelred_died_after_704_was_King_of_Mercia | type | Person |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Oshere | hasParent | Osthryth |
| Oshere | type | Agent |
| Oshere | type | Person |
| Osthryth | hasChild | Oshere |
| Osthryth | hasSpouse | Æthelred_died_after_704_was_King_of_Mercia |
| Osthryth | type | Agent |
| Osthryth | type | Person |
| Æthelred_died_after_704_was_King_of_Mercia | hasSpouse | Osthryth |

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Æthelred_died_after_704_was_King_of_Mercia | hasChild | osric_hwicce |
| Æthelred_died_after_704_was_King_of_Mercia | hasChild | oswald_hwicce |
| osric_hwicce | hasParent | Æthelred_died_after_704_was_King_of_Mercia |
| osric_hwicce | type | Agent |
| osric_hwicce | type | Person |
| oswald_hwicce | hasParent | Æthelred_died_after_704_was_King_of_Mercia |
| oswald_hwicce | type | Agent |
| oswald_hwicce | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 1 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 18 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 8 |
| Precision | 0.200000 |
| Recall | 0.200000 |
| F1 score | 0.200000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
