# Triple matching report: 439

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Can_t_Remember_to_Forget_You | hasPublicationDate | "2014-01-13"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Distant_Lover | hasPublicationDate | "1974"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Can_t_Remember_to_Forget_You | type | MusicalWork |
| Can_t_Remember_to_Forget_You | type | NamedIndividual |
| Can_t_Remember_to_Forget_You | label | "Can't Remember To Forget You" |
| Distant_Lover | hasPublicationDate | "1973"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Distant_Lover | type | MusicalWork |
| Distant_Lover | type | NamedIndividual |
| Distant_Lover | label | "Distant Lover" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.125000 |
| Recall | 0.500000 |
| F1 score | 0.200000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
