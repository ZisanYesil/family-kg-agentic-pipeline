# Triple matching report: 379

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Maria_Cristina_Infanta_of_Spain | type | Agent |
| Maria_Cristina_Infanta_of_Spain | type | Person |
| Princess_Luisa_Carlotta_of_Naples_and_Sicily | type | Agent |
| Princess_Luisa_Carlotta_of_Naples_and_Sicily | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Infante_Francisco_de_Paula_of_Spain | hasChild | Maria_Cristina_Infanta_of_Spain |
| Infante_Francisco_de_Paula_of_Spain | hasSpouse | Princess_Luisa_Carlotta_of_Naples_and_Sicily |
| Infante_Francisco_de_Paula_of_Spain | type | Agent |
| Infante_Francisco_de_Paula_of_Spain | type | Person |
| Maria_Cristina_Infanta_of_Spain | hasParent | Infante_Francisco_de_Paula_of_Spain |
| Princess_Luisa_Carlotta_of_Naples_and_Sicily | hasSpouse | Infante_Francisco_de_Paula_of_Spain |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Maria_Cristina_Infanta_of_Spain | hasParent | Princess_Luisa_Carlotta_of_Naples_and_Sicily |
| Princess_Luisa_Carlotta_of_Naples_and_Sicily | hasChild | Maria_Cristina_Infanta_of_Spain |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.666667 |
| Recall | 0.400000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
