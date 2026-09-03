# Triple matching report: 416

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Agnes_of_Meissen | hasParent | Margaret_of_Sicily |
| Agnes_of_Meissen | type | Agent |
| Agnes_of_Meissen | type | Person |
| Margaret_of_Sicily | hasChild | Agnes_of_Meissen |
| Margaret_of_Sicily | type | Agent |
| Margaret_of_Sicily | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Germany | type | Country |
| Germany | type | Place |
| Margaret_of_Sicily | hasCountry | Germany |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Margaret_of_Sicily | hasCountry | sicily |
| sicily | type | Country |
| sicily | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 12 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.666667 |
| Recall | 0.666667 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
