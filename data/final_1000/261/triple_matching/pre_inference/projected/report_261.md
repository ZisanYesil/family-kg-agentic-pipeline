# Triple matching report: 261

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Kalakalappu_2 | hasPublicationDate | "2018"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Kuch_Kuch_Hota_Hai | hasPublicationDate | "1998"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Kalakalappu_2 | type | Film |
| Kalakalappu_2 | type | NamedIndividual |
| Kalakalappu_2 | label | "Kalakalappu 2" |
| Kuch_Kuch_Hota_Hai | type | Film |
| Kuch_Kuch_Hota_Hai | type | NamedIndividual |
| Kuch_Kuch_Hota_Hai | label | "Kuch Kuch Hota Hai" |
| Kuch_Kuch_Hota_Hai | altLabel | "KKHH" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
