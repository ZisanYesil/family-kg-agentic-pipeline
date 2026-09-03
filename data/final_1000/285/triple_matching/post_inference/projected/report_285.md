# Triple matching report: 285

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| British | type | Country |
| British | type | Place |
| Starter_for_10_film | hasCountry | British |
| Starter_for_10_film | type | Artifact |
| The_Urethra_Chronicles | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Starter_for_10_film | hasCountry | US |
| The_Urethra_Chronicles | hasCountry | American |
| US | type | Country |
| US | type | Place |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Starter_for_10_film | type | CreativeWork |
| Starter_for_10_film | type | Film |
| The_Urethra_Chronicles | type | CreativeWork |
| The_Urethra_Chronicles | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 15 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.555556 |
| Recall | 0.454545 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
