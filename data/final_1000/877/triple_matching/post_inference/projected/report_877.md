# Triple matching report: 877

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Article_99 | hasCountry | American |
| Article_99 | type | Artifact |
| Six_Dance_Lessons_in_Six_Weeks_film | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Hungarian | type | Country |
| Hungarian | type | Place |
| Six_Dance_Lessons_in_Six_Weeks_film | hasCountry | Hungarian |

## 2.2 Extracted-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Article_99 | type | CreativeWork |
| Article_99 | type | Film |
| Six_Dance_Lessons_in_Six_Weeks_film | hasCountry | American |
| Six_Dance_Lessons_in_Six_Weeks_film | type | CreativeWork |
| Six_Dance_Lessons_in_Six_Weeks_film | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 13 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 5 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.500000 |
| Recall | 0.625000 |
| F1 score | 0.555556 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
