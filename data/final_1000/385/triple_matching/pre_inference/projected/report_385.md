# Triple matching report: 385

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Vladimír_Godár | hasCountry | Slovak |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Let_asfaltového_holuba | hasComposer | Vladimír_Godár |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Let_asfaltového_holuba | hasCreator | Vladimír_Godár |
| Let_asfaltového_holuba | type | Film |
| Let_asfaltového_holuba | type | NamedIndividual |
| Let_asfaltového_holuba | label | "Let asfaltového holuba" |
| Slovak | type | Country |
| Slovak | type | NamedIndividual |
| Slovak | label | "Slovakia" |
| Slovak | altLabel | "Slovak" |
| Vladimír_Godár | type | Person |
| Vladimír_Godár | type | NamedIndividual |
| Vladimír_Godár | label | "Vladimír Godár" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
