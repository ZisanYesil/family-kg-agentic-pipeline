# Triple matching report: 985

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Elisabeth_Magdalena_of_Pomerania | hasParent | Ernst_Ludwig_Duke_of_Pomerania |
| Ernst_Ludwig_Duke_of_Pomerania | hasBirthPlace | Wolgast |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Elisabeth_Magdalena_of_Pomerania | type | Person |
| Elisabeth_Magdalena_of_Pomerania | type | NamedIndividual |
| Elisabeth_Magdalena_of_Pomerania | label | "Elisabeth Magdalena of Pomerania" |
| Elisabeth_Magdalena_of_Pomerania | altLabel | "Elisabeth Magdalena Of Pomerania" |
| Ernst_Ludwig_Duke_of_Pomerania | type | Person |
| Ernst_Ludwig_Duke_of_Pomerania | type | NamedIndividual |
| Ernst_Ludwig_Duke_of_Pomerania | label | "Ernst Ludwig" |
| Ernst_Ludwig_Duke_of_Pomerania | altLabel | "Ernst Ludwig, Duke of Pomerania" |
| Wolgast | type | Place |
| Wolgast | type | NamedIndividual |
| Wolgast | label | "Wolgast" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
