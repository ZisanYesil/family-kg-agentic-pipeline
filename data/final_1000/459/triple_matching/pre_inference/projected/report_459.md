# Triple matching report: 459

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Peter_II_Count_of_Saint_Pol | hasParent | Jeanne_de_Bar_Countess_of_Marle_and_Soissons |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Jeanne_de_Bar_suo_jure_Countess_of_Marle_and_Soissons | hasBirthPlace | French |

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Jeanne_de_Bar_Countess_of_Marle_and_Soissons | type | Person |
| Jeanne_de_Bar_Countess_of_Marle_and_Soissons | type | NamedIndividual |
| Jeanne_de_Bar_Countess_of_Marle_and_Soissons | label | "Jeanne de Bar, Countess of Marle and Soissons" |
| Jeanne_de_Bar_Countess_of_Marle_and_Soissons | altLabel | "Jeanne de Bar" |
| Peter_II_Count_of_Saint_Pol | type | Person |
| Peter_II_Count_of_Saint_Pol | type | NamedIndividual |
| Peter_II_Count_of_Saint_Pol | label | "Peter II, Count of Saint-Pol" |
| Peter_II_Count_of_Saint_Pol | altLabel | "Peter II" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.111111 |
| Recall | 0.500000 |
| F1 score | 0.181818 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
