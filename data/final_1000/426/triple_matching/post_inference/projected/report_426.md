# Triple matching report: 426

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Bombshell_The_Hedy_Lamarr_Story | hasCountry | American |
| Bombshell_The_Hedy_Lamarr_Story | type | Artifact |
| Czech | type | Country |
| Czech | type | Place |
| Toman_film | hasCountry | Czech |
| Toman_film | type | Artifact |

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
| Bombshell_The_Hedy_Lamarr_Story | type | CreativeWork |
| Bombshell_The_Hedy_Lamarr_Story | type | Film |
| Toman_film | type | CreativeWork |
| Toman_film | type | Film |

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
