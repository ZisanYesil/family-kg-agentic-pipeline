# Triple matching report: 377

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Isabelle_of_Luxembourg | hasChild | John_I_Marquis_of_Namur |
| Isabelle_of_Luxembourg | type | Agent |
| Isabelle_of_Luxembourg | type | Person |
| John_II_of_Namur | hasParent | John_I_Marquis_of_Namur |
| John_II_of_Namur | type | Agent |
| John_II_of_Namur | type | Person |
| John_I_Marquis_of_Namur | hasChild | John_II_of_Namur |
| John_I_Marquis_of_Namur | hasParent | Isabelle_of_Luxembourg |
| John_I_Marquis_of_Namur | type | Agent |
| John_I_Marquis_of_Namur | type | Person |

# 2. Unmatched triples

**Total unmatched count: 0**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 10 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 0 |
| Precision | 1.000000 |
| Recall | 1.000000 |
| F1 score | 1.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
