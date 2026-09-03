# Triple matching report: 459

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Jeanne_de_Bar_Countess_of_Marle_and_Soissons | hasChild | Peter_II_Count_of_Saint_Pol |
| Jeanne_de_Bar_Countess_of_Marle_and_Soissons | type | Agent |
| Jeanne_de_Bar_Countess_of_Marle_and_Soissons | type | Person |
| Peter_II_Count_of_Saint_Pol | hasParent | Jeanne_de_Bar_Countess_of_Marle_and_Soissons |
| Peter_II_Count_of_Saint_Pol | type | Agent |
| Peter_II_Count_of_Saint_Pol | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| French | type | Place |
| Jeanne_de_Bar_suo_jure_Countess_of_Marle_and_Soissons | hasBirthPlace | French |
| Jeanne_de_Bar_suo_jure_Countess_of_Marle_and_Soissons | type | Agent |
| Jeanne_de_Bar_suo_jure_Countess_of_Marle_and_Soissons | type | Person |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 10 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 4 |
| Precision | 1.000000 |
| Recall | 0.600000 |
| F1 score | 0.750000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
