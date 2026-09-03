# Triple matching report: 558

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Sybilla_of_Burgundy | hasParent | William_I_Count_of_Burgundy |
| William_I_Count_of_Burgundy | hasParent | Alice_of_Normandy |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Alice_of_Normandy | type | Person |
| Alice_of_Normandy | type | NamedIndividual |
| Alice_of_Normandy | label | "Alice of Normandy" |
| Alice_of_Normandy | altLabel | "Alice of Normandy" |
| Sybilla_of_Burgundy | type | Person |
| Sybilla_of_Burgundy | type | NamedIndividual |
| Sybilla_of_Burgundy | label | "Sybilla of Burgundy" |
| Sybilla_of_Burgundy | altLabel | "Sibylla of Burgundy" |
| Sybilla_of_Burgundy | altLabel | "Sybilla of Burgundy" |
| William_I_Count_of_Burgundy | type | Person |
| William_I_Count_of_Burgundy | type | NamedIndividual |
| William_I_Count_of_Burgundy | label | "William I, Count of Burgundy" |
| William_I_Count_of_Burgundy | altLabel | "William I, Count of Burgundy" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
