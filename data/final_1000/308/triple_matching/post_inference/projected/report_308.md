# Triple matching report: 308

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Duke_Henry_of_Mecklenburg_Schwerin | type | Agent |
| Duke_Henry_of_Mecklenburg_Schwerin | type | Person |
| Juliana_of_the_Netherlands | type | Agent |
| Juliana_of_the_Netherlands | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Duke_Henry_of_Mecklenburg_Schwerin | hasSpouse | Wilhelmina |
| Juliana_of_the_Netherlands | hasParent | Wilhelmina |
| Wilhelmina | hasChild | Juliana_of_the_Netherlands |
| Wilhelmina | hasSpouse | Duke_Henry_of_Mecklenburg_Schwerin |
| Wilhelmina | type | Agent |
| Wilhelmina | type | Person |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Duke_Henry_of_Mecklenburg_Schwerin | hasChild | Juliana_of_the_Netherlands |
| Juliana_of_the_Netherlands | hasParent | Duke_Henry_of_Mecklenburg_Schwerin |

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
