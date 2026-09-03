# Triple matching report: 683

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Alfons_Zitterbacke | type | Artifact |
| German | type | Country |
| German | type | Place |
| The_Almighty_Dollar_1923_film | hasCountry | German |
| The_Almighty_Dollar_1923_film | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Alfons_Zitterbacke | hasCountry | German |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Alfons_Zitterbacke | hasCountry | country_east_germany |
| Alfons_Zitterbacke | type | CreativeWork |
| Alfons_Zitterbacke | type | Film |
| The_Almighty_Dollar_1923_film | type | CreativeWork |
| The_Almighty_Dollar_1923_film | type | Film |
| country_east_germany | type | Country |
| country_east_germany | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 13 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.416667 |
| Recall | 0.833333 |
| F1 score | 0.555556 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
