# Triple matching report: 203

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| British | type | Country |
| British | type | Place |
| Lover_s_Prayer | hasCountry | American |
| Lover_s_Prayer | hasCountry | British |
| Lover_s_Prayer | type | Artifact |
| Make_Up_1937_film | hasCountry | British |
| Make_Up_1937_film | type | Artifact |

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
| Lover_s_Prayer | type | CreativeWork |
| Lover_s_Prayer | type | Film |
| Make_Up_1937_film | type | CreativeWork |
| Make_Up_1937_film | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 13 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.692308 |
| Recall | 1.000000 |
| F1 score | 0.818182 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
