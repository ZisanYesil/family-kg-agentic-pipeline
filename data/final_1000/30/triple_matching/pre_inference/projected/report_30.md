# Triple matching report: 30

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Los_Motivos_de_Luz | hasDirector | Felipe_Cazals |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Felipe_Cazals | hasBirthPlace | France |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Felipe_Cazals | hasBirthPlace | place_mexico_df |
| Felipe_Cazals | type | Person |
| Felipe_Cazals | type | NamedIndividual |
| Felipe_Cazals | label | "Felipe Cazals" |
| Los_Motivos_de_Luz | type | Film |
| Los_Motivos_de_Luz | type | NamedIndividual |
| Los_Motivos_de_Luz | label | "Los Motivos de Luz" |
| place_mexico_df | type | Place |
| place_mexico_df | type | NamedIndividual |
| place_mexico_df | label | "Mexico, D.F." |
| place_mexico_df | altLabel | "Mexico D.F." |
| place_mexico_df | altLabel | "Mexico, D.F." |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
