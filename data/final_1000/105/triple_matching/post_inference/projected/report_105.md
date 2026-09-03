# Triple matching report: 105

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| God_s_Ears | type | Artifact |
| The_Keeper_of_the_Bees_1935_film | hasCountry | American |
| The_Keeper_of_the_Bees_1935_film | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| God_s_Ears | hasCountry | American |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| God_s_Ears | type | CreativeWork |
| God_s_Ears | type | Film |
| The_Keeper_of_the_Bees_1935_film | type | CreativeWork |
| The_Keeper_of_the_Bees_1935_film | type | Film |

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
