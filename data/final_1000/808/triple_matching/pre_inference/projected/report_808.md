# Triple matching report: 808

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Colonel_Abrams_album | hasPublicationDate | "1985"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Eto_Baš_hoću | hasPublicationDate | "1976"^^<http://www.w3.org/2001/XMLSchema#gYear> |

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
| Colonel_Abrams_album | type | CreativeWork |
| Colonel_Abrams_album | type | NamedIndividual |
| Colonel_Abrams_album | label | "Colonel Abrams" |
| Colonel_Abrams_album | altLabel | "Colonel Abrams" |
| Eto_Baš_hoću | type | CreativeWork |
| Eto_Baš_hoću | type | NamedIndividual |
| Eto_Baš_hoću | label | "Eto! Baš hoću!" |
| Eto_Baš_hoću | altLabel | "Eto! Baš hoću!" |

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
