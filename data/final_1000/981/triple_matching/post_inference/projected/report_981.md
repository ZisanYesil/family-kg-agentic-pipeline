# Triple matching report: 981

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Eleanor_of_Arborea | type | Agent |
| Eleanor_of_Arborea | type | Person |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Brancaleone_Doria | hasChild | Frederick_1377_1387_was_the_Judge_of_Arborea |
| Brancaleone_Doria | hasSpouse | Eleanor_of_Arborea |
| Brancaleone_Doria | type | Agent |
| Brancaleone_Doria | type | Person |
| Eleanor_of_Arborea | hasSpouse | Brancaleone_Doria |
| Frederick_1377_1387_was_the_Judge_of_Arborea | hasParent | Brancaleone_Doria |
| Frederick_1377_1387_was_the_Judge_of_Arborea | type | Agent |
| Frederick_1377_1387_was_the_Judge_of_Arborea | type | Person |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Eleanor_of_Arborea | hasChild | frederick_of_arborea |
| frederick_of_arborea | hasParent | Eleanor_of_Arborea |
| frederick_of_arborea | type | Agent |
| frederick_of_arborea | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 1 |
| Extracted triples in scope | 6 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 8 |
| Precision | 0.333333 |
| Recall | 0.200000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
