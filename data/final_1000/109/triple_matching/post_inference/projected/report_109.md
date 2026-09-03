# Triple matching report: 109

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| The_Christian_Licorice_Store | hasCountry | American |
| The_Christian_Licorice_Store | type | Artifact |
| The_Crime_of_Korea | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| The_Crime_of_Korea | hasCountry | US |
| US | type | Country |
| US | type | Place |

## 2.2 Extracted-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| The_Christian_Licorice_Store | type | CreativeWork |
| The_Christian_Licorice_Store | type | Film |
| The_Crime_of_Korea | hasCountry | American |
| The_Crime_of_Korea | type | CreativeWork |
| The_Crime_of_Korea | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 13 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 5 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.500000 |
| Recall | 0.625000 |
| F1 score | 0.555556 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
