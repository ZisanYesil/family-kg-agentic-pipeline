# Triple matching report: 30

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Felipe_Cazals | type | Agent |
| Felipe_Cazals | type | Person |
| Los_Motivos_de_Luz | hasCreator | Felipe_Cazals |
| Los_Motivos_de_Luz | hasDirector | Felipe_Cazals |
| Los_Motivos_de_Luz | type | Artifact |
| Los_Motivos_de_Luz | type | CreativeWork |
| Los_Motivos_de_Luz | type | Film |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Felipe_Cazals | hasBirthPlace | France |
| France | type | Place |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Felipe_Cazals | hasBirthPlace | place_mexico_df |
| place_mexico_df | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 11 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.777778 |
| Recall | 0.777778 |
| F1 score | 0.777778 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
