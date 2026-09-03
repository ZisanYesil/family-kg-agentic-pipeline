# Triple matching report: 695

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Margaret_Countess_of_Anjou | hasSpouse | Charles_of_Valois |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Charles_of_Valois | hasCountry | France |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Charles_of_Valois | type | Person |
| Charles_of_Valois | type | NamedIndividual |
| Charles_of_Valois | label | "Charles of Valois" |
| Margaret_Countess_of_Anjou | type | Person |
| Margaret_Countess_of_Anjou | type | NamedIndividual |
| Margaret_Countess_of_Anjou | label | "Margaret, Countess of Anjou" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 8 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.142857 |
| Recall | 0.500000 |
| F1 score | 0.222222 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
