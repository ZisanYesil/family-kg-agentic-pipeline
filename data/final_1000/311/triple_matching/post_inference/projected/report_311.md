# Triple matching report: 311

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| French | type | Country |
| French | type | Place |
| My_Father_the_Hero_1994_film | hasCountry | American |
| My_Father_the_Hero_1994_film | hasCountry | French |
| My_Father_the_Hero_1994_film | type | Artifact |
| Wyoming_Roundup | hasCountry | American |
| Wyoming_Roundup | type | Artifact |

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
| My_Father_the_Hero_1994_film | type | CreativeWork |
| My_Father_the_Hero_1994_film | type | Film |
| Wyoming_Roundup | type | CreativeWork |
| Wyoming_Roundup | type | Film |

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
