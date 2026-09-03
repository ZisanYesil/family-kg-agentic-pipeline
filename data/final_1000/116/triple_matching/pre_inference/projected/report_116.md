# Triple matching report: 116

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| The_Collector_2002_film | hasCountry | Canadian |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Gulîstan_Land_of_Roses | hasCountry | Canadian |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Canadian | type | Country |
| Canadian | type | NamedIndividual |
| Canadian | label | "Canada" |
| Canadian | altLabel | "Canadian" |
| Gulîstan_Land_of_Roses | type | Film |
| Gulîstan_Land_of_Roses | type | NamedIndividual |
| Gulîstan_Land_of_Roses | label | "Gulîstan, Land Of Roses" |
| The_Collector_2002_film | type | Film |
| The_Collector_2002_film | type | NamedIndividual |
| The_Collector_2002_film | label | "The Collector (2002 film)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
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
