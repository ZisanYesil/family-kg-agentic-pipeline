# Triple matching report: 167

# 1. Matched triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| Black_Gravel | hasCreator | Helmut_Käutner |
| Black_Gravel | hasDirector | Helmut_Käutner |
| Black_Gravel | type | Artifact |
| Black_Gravel | type | CreativeWork |
| Black_Gravel | type | Film |
| Georg_Jacoby | type | Agent |
| Georg_Jacoby | type | Person |
| Germany | type | Country |
| Germany | type | Place |
| Helmut_Käutner | hasCountry | Germany |
| Helmut_Käutner | type | Agent |
| Helmut_Käutner | type | Person |
| The_Little_Napoleon | hasCreator | Georg_Jacoby |
| The_Little_Napoleon | hasDirector | Georg_Jacoby |
| The_Little_Napoleon | type | Artifact |
| The_Little_Napoleon | type | CreativeWork |
| The_Little_Napoleon | type | Film |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Georg_Jacoby | hasCountry | German |
| German | type | Country |
| German | type | Place |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Georg_Jacoby | hasCountry | Germany |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 20 |
| Union triples in scope | 21 |
| True positives (matched) | 17 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.944444 |
| Recall | 0.850000 |
| F1 score | 0.894737 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
