# Triple matching report: 516

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| The_To_Do_List | hasCountry | American |
| The_To_Do_List | type | Artifact |
| The_Twelve_Chairs_1970_film | hasCountry | American |
| The_Twelve_Chairs_1970_film | type | Artifact |

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
| The_To_Do_List | type | CreativeWork |
| The_To_Do_List | type | Film |
| The_Twelve_Chairs_1970_film | type | CreativeWork |
| The_Twelve_Chairs_1970_film | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 10 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.600000 |
| Recall | 1.000000 |
| F1 score | 0.750000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
