# Triple matching report: 461

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Louise_Marie_Thérèse_d_Artois | hasParent | Princess_Caroline_of_Naples_and_Sicily |
| Louise_Marie_Thérèse_d_Artois | type | Agent |
| Louise_Marie_Thérèse_d_Artois | type | Person |
| Princess_Caroline_of_Naples_and_Sicily | hasChild | Louise_Marie_Thérèse_d_Artois |
| Princess_Caroline_of_Naples_and_Sicily | type | Agent |
| Princess_Caroline_of_Naples_and_Sicily | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Italian | type | Country |
| Italian | type | Place |
| Marie_Caroline_de_Bourbon_Sicile_duchesse_de_Berry | hasCountry | Italian |
| Marie_Caroline_de_Bourbon_Sicile_duchesse_de_Berry | type | Agent |
| Marie_Caroline_de_Bourbon_Sicile_duchesse_de_Berry | type | Person |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Princess_Caroline_of_Naples_and_Sicily | hasCountry | naples_and_sicily |
| naples_and_sicily | type | Country |
| naples_and_sicily | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 14 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 5 |
| Precision | 0.666667 |
| Recall | 0.545455 |
| F1 score | 0.600000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
