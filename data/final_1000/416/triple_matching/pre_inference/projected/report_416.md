# Triple matching report: 416

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Agnes_of_Meissen | hasParent | Margaret_of_Sicily |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Margaret_of_Sicily | hasCountry | Germany |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Agnes_of_Meissen | type | Person |
| Agnes_of_Meissen | type | NamedIndividual |
| Agnes_of_Meissen | label | "Agnes of Meissen" |
| Margaret_of_Sicily | hasCountry | sicily |
| Margaret_of_Sicily | type | Person |
| Margaret_of_Sicily | type | NamedIndividual |
| Margaret_of_Sicily | label | "Margaret of Sicily" |
| sicily | type | Country |
| sicily | type | NamedIndividual |
| sicily | label | "Sicily" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
