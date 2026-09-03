# Triple matching report: 830

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_Plantagenet_1st_Viscount_Lisle | hasParent | Edward_IV |
| Edward_IV | hasSpouse | Elizabeth_Woodville |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Arthur_Plantagenet_1st_Viscount_Lisle | type | Person |
| Arthur_Plantagenet_1st_Viscount_Lisle | type | NamedIndividual |
| Arthur_Plantagenet_1st_Viscount_Lisle | label | "Arthur Plantagenet, 1st Viscount Lisle" |
| Edward_IV | type | Person |
| Edward_IV | type | NamedIndividual |
| Edward_IV | label | "Edward IV of England" |
| Elizabeth_Woodville | type | Person |
| Elizabeth_Woodville | type | NamedIndividual |
| Elizabeth_Woodville | label | "Elizabeth Woodville" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
