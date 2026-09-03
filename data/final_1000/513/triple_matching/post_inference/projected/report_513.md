# Triple matching report: 513

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Bécassine_2018_film | hasCountry | French |
| Bécassine_2018_film | type | Artifact |
| French | type | Country |
| French | type | Place |
| The_Smell_of_Us | hasCountry | French |
| The_Smell_of_Us | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Bécassine_2018_film | type | CreativeWork |
| Bécassine_2018_film | type | Film |
| The_Smell_of_Us | type | CreativeWork |
| The_Smell_of_Us | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 10 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.600000 |
| Recall | 1.000000 |
| F1 score | 0.750000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
