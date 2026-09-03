# Triple matching report: 439

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Can_t_Remember_to_Forget_You | hasPublicationDate | "2014-01-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Can_t_Remember_to_Forget_You | type | Artifact |
| Can_t_Remember_to_Forget_You | type | CreativeWork |
| Distant_Lover | type | Artifact |
| Distant_Lover | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Distant_Lover | hasPublicationDate | "1974"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Can_t_Remember_to_Forget_You | type | MusicalWork |
| Distant_Lover | hasPublicationDate | "1973"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Distant_Lover | type | MusicalWork |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 9 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.625000 |
| Recall | 0.833333 |
| F1 score | 0.714286 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
