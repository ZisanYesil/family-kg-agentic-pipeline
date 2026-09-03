# Triple matching report: 138

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| German | type | Country |
| German | type | Place |
| Heart_of_Stone_1950_film | hasCountry | German |
| Heart_of_Stone_1950_film | type | Artifact |
| The_Plaything_of_Broadway | hasCountry | American |
| The_Plaything_of_Broadway | type | Artifact |

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
| Heart_of_Stone_1950_film | type | CreativeWork |
| Heart_of_Stone_1950_film | type | Film |
| The_Plaything_of_Broadway | type | CreativeWork |
| The_Plaything_of_Broadway | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 12 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.666667 |
| Recall | 1.000000 |
| F1 score | 0.800000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
