# Triple matching report: 779

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Disaster_Movie | hasCountry | American |
| Disaster_Movie | type | Artifact |
| Hacker_film | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Hacker_film | hasCountry | Hong_Kong |
| Hong_Kong | type | Country |
| Hong_Kong | type | Place |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Disaster_Movie | type | CreativeWork |
| Disaster_Movie | type | Film |
| Hacker_film | type | CreativeWork |
| Hacker_film | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 12 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.555556 |
| Recall | 0.625000 |
| F1 score | 0.588235 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
