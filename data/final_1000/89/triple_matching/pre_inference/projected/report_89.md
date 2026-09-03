# Triple matching report: 89

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Grand_Duchess_Natalya_Alexeyevna_of_Russia | hasSibling | Peter_II_of_Russia |
| Peter_II_of_Russia | hasParent | Charlotte_Christine_of_Brunswick_Lüneburg |

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
| Charlotte_Christine_of_Brunswick_Lüneburg | type | Person |
| Charlotte_Christine_of_Brunswick_Lüneburg | type | NamedIndividual |
| Charlotte_Christine_of_Brunswick_Lüneburg | label | "Charlotte Christine of Brunswick-Lüneburg" |
| Grand_Duchess_Natalya_Alexeyevna_of_Russia | type | Person |
| Grand_Duchess_Natalya_Alexeyevna_of_Russia | type | NamedIndividual |
| Grand_Duchess_Natalya_Alexeyevna_of_Russia | label | "Grand Duchess Natalya Alexeyevna of Russia" |
| Grand_Duchess_Natalya_Alexeyevna_of_Russia | altLabel | "Natalya Alexeyevna (1714–1728)" |
| Peter_II_of_Russia | type | Person |
| Peter_II_of_Russia | type | NamedIndividual |
| Peter_II_of_Russia | label | "Peter II of Russia" |
| Peter_II_of_Russia | altLabel | "Peter II Alexeyevich" |

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
