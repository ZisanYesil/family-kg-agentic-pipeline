# Triple matching report: 126

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| A_R_Reihana | hasChild | G_V_Prakash_Kumar |
| A_R_Reihana | type | Agent |
| A_R_Reihana | type | Person |
| G_V_Prakash_Kumar | hasParent | A_R_Reihana |
| G_V_Prakash_Kumar | type | Agent |
| G_V_Prakash_Kumar | type | Person |
| Machi | hasComposer | A_R_Reihana |
| Machi | hasCreator | A_R_Reihana |
| Machi | type | Artifact |
| Machi | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| A_R_Reihana | hasChild | person_bhavani_sree |
| Machi | type | Film |
| person_bhavani_sree | hasParent | A_R_Reihana |
| person_bhavani_sree | type | Agent |
| person_bhavani_sree | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 15 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 5 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.666667 |
| Recall | 1.000000 |
| F1 score | 0.800000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
