# Triple matching report: 195

# 1. Matched triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| German | type | Country |
| German | type | Place |
| Mystery_Plane | hasCountry | American |
| Mystery_Plane | type | Artifact |
| Soviet | type | Country |
| Soviet | type | Place |
| To_Kill_a_Dragon | hasCountry | German |
| To_Kill_a_Dragon | hasCountry | Soviet |
| To_Kill_a_Dragon | type | Artifact |

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
| Mystery_Plane | type | CreativeWork |
| Mystery_Plane | type | Film |
| To_Kill_a_Dragon | type | CreativeWork |
| To_Kill_a_Dragon | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 15 |
| True positives (matched) | 11 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.733333 |
| Recall | 1.000000 |
| F1 score | 0.846154 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
