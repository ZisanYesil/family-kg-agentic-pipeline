# Triple matching report: 262

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Free_China_Journal | hasInception | "1949"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Neue_Grafik | hasInception | "1958"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| free_china_journal | hasPublicationDate | "1949"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| free_china_journal | type | CreativeWork |
| free_china_journal | type | NamedIndividual |
| free_china_journal | label | "Free China Journal" |
| neue_grafik | hasPublicationDate | "1958"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| neue_grafik | type | CreativeWork |
| neue_grafik | type | NamedIndividual |
| neue_grafik | label | "Neue Grafik" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 0 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
