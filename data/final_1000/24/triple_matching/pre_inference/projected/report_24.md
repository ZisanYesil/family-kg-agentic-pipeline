# Triple matching report: 24

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Philippa_de_Beauchamp | hasSpouse | Hugh_de_Stafford_2nd_Earl_of_Stafford |
| Thomas_Stafford_3rd_Earl_of_Stafford | hasParent | Philippa_de_Beauchamp |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Hugh_de_Stafford_2nd_Earl_of_Stafford | type | Person |
| Hugh_de_Stafford_2nd_Earl_of_Stafford | type | NamedIndividual |
| Hugh_de_Stafford_2nd_Earl_of_Stafford | label | "Hugh Stafford, 2nd Earl of Stafford" |
| Hugh_de_Stafford_2nd_Earl_of_Stafford | altLabel | "Hugh Stafford" |
| Thomas_Stafford_3rd_Earl_of_Stafford | hasParent | Hugh_de_Stafford_2nd_Earl_of_Stafford |
| Thomas_Stafford_3rd_Earl_of_Stafford | type | Person |
| Thomas_Stafford_3rd_Earl_of_Stafford | type | NamedIndividual |
| Thomas_Stafford_3rd_Earl_of_Stafford | label | "Thomas Stafford, 3rd Earl of Stafford" |
| Thomas_Stafford_3rd_Earl_of_Stafford | altLabel | "Thomas Stafford" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
