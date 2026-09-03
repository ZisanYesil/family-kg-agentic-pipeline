# Triple matching report: 762

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Blanche_of_France_Duchess_of_Orléans | hasParent | Jeanne_d_Évreux |
| Jeanne_d_Évreux | hasParent | Louis_Count_of_Évreux |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Blanche_of_France_Duchess_of_Orléans | type | Person |
| Blanche_of_France_Duchess_of_Orléans | type | NamedIndividual |
| Blanche_of_France_Duchess_of_Orléans | label | "Blanche of France, Duchess of Orléans" |
| Jeanne_d_Évreux | type | Person |
| Jeanne_d_Évreux | type | NamedIndividual |
| Jeanne_d_Évreux | label | "Jeanne d'Évreux" |
| Louis_Count_of_Évreux | type | Person |
| Louis_Count_of_Évreux | type | NamedIndividual |
| Louis_Count_of_Évreux | label | "Louis, Count of Évreux" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
