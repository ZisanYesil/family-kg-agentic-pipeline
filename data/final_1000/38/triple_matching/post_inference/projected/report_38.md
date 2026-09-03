# Triple matching report: 38

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Johan_Jacobsen | type | Agent |
| Johan_Jacobsen | type | Person |
| Min_kone_er_uskyldig | hasCreator | Johan_Jacobsen |
| Min_kone_er_uskyldig | hasDirector | Johan_Jacobsen |
| Min_kone_er_uskyldig | type | Artifact |
| Min_kone_er_uskyldig | type | CreativeWork |
| Min_kone_er_uskyldig | type | Film |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Annelise_Hovmand | hasSpouse | Johan_Jacobsen |
| Annelise_Hovmand | type | Agent |
| Annelise_Hovmand | type | Person |
| Johan_Jacobsen | hasSpouse | Annelise_Hovmand |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 11 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 4 |
| Precision | 1.000000 |
| Recall | 0.636364 |
| F1 score | 0.777778 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
