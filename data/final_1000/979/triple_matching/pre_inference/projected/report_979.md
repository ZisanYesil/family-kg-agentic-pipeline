# Triple matching report: 979

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Fernando_Cortés | hasSpouse | Mapy_Cortés |
| The_Phantom_of_the_Operetta | hasDirector | Fernando_Cortés |

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
| Fernando_Cortés | type | Person |
| Fernando_Cortés | type | NamedIndividual |
| Fernando_Cortés | label | "Fernando Cortés" |
| Fernando_Cortés | altLabel | "Fernando \"Papi\" Cortés" |
| Mapy_Cortés | type | Person |
| Mapy_Cortés | type | NamedIndividual |
| Mapy_Cortés | label | "María del Pilar Cordero" |
| Mapy_Cortés | altLabel | "Mapy Cortés" |
| The_Phantom_of_the_Operetta | type | Film |
| The_Phantom_of_the_Operetta | type | NamedIndividual |
| The_Phantom_of_the_Operetta | label | "The Phantom of the Operetta (1960 film)" |

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
