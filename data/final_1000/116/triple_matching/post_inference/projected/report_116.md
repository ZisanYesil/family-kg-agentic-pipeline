# Triple matching report: 116

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Canadian | type | Country |
| Canadian | type | Place |
| Gulîstan_Land_of_Roses | type | Artifact |
| The_Collector_2002_film | hasCountry | Canadian |
| The_Collector_2002_film | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Gulîstan_Land_of_Roses | hasCountry | Canadian |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Gulîstan_Land_of_Roses | type | CreativeWork |
| Gulîstan_Land_of_Roses | type | Film |
| The_Collector_2002_film | type | CreativeWork |
| The_Collector_2002_film | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 10 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.555556 |
| Recall | 0.833333 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
