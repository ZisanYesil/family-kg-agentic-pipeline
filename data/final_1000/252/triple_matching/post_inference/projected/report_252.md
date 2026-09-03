# Triple matching report: 252

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| German | type | Country |
| German | type | Place |
| Tannenberg_film | hasCountry | German |
| Tannenberg_film | type | Artifact |
| To_Kill_a_Dragon | hasCountry | German |
| To_Kill_a_Dragon | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Soviet | type | Country |
| Soviet | type | Place |
| To_Kill_a_Dragon | hasCountry | Soviet |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Tannenberg_film | type | CreativeWork |
| Tannenberg_film | type | Film |
| To_Kill_a_Dragon | type | CreativeWork |
| To_Kill_a_Dragon | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 13 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.600000 |
| Recall | 0.666667 |
| F1 score | 0.631579 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
