# Triple matching report: 504

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Heart_of_Paris | hasPublicationDate | "1932"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Padithal_Mattum_Podhuma | hasPublicationDate | "1962"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Heart_of_Paris | type | Film |
| Heart_of_Paris | type | NamedIndividual |
| Heart_of_Paris | label | "Heart of Paris" |
| Heart_of_Paris | altLabel | "Coeur de Paris" |
| Padithal_Mattum_Podhuma | type | Film |
| Padithal_Mattum_Podhuma | type | NamedIndividual |
| Padithal_Mattum_Podhuma | label | "Padithal Mattum Podhuma" |
| Padithal_Mattum_Podhuma | altLabel | "Padithaal Mattum Podhuma" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
