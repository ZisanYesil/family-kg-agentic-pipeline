# Triple matching report: 680

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| British | type | Country |
| British | type | Place |
| Four_Eyed_Monsters | hasCountry | American |
| Four_Eyed_Monsters | type | Artifact |
| Joseph_and_the_Amazing_Technicolor_Dreamcoat_film | hasCountry | British |
| Joseph_and_the_Amazing_Technicolor_Dreamcoat_film | type | Artifact |

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
| Four_Eyed_Monsters | type | CreativeWork |
| Four_Eyed_Monsters | type | Film |
| Joseph_and_the_Amazing_Technicolor_Dreamcoat_film | type | CreativeWork |
| Joseph_and_the_Amazing_Technicolor_Dreamcoat_film | type | Film |

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
