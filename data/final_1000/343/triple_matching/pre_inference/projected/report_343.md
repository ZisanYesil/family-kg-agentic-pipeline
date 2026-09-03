# Triple matching report: 343

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Philippa_of_Hainault | hasCauseOfDeath | edema |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Joan_of_England | hasParent | Philippa_of_Hainault |

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Joan_of_England | type | Person |
| Joan_of_England | type | NamedIndividual |
| Joan_of_England | label | "Joan of England" |
| Joan_of_England | altLabel | "Joan of England (1333/34–1348)" |
| Joan_of_England | altLabel | "Joan of England (1335–1348)" |
| Philippa_of_Hainault | hasChild | Joan_of_England |
| Philippa_of_Hainault | type | Person |
| Philippa_of_Hainault | type | NamedIndividual |
| Philippa_of_Hainault | label | "Philippa of Hainault" |
| Philippa_of_Hainault | altLabel | "Philippa of Hainault" |
| edema | type | CauseOfDeath |
| edema | type | NamedIndividual |
| edema | label | "Illness closely related to edema" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.071429 |
| Recall | 0.500000 |
| F1 score | 0.125000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
