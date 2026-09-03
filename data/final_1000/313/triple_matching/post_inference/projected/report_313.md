# Triple matching report: 313

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| En_sømand_går_i_land | hasPublicationDate | "1954"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| En_sømand_går_i_land | type | Artifact |
| En_sømand_går_i_land | type | CreativeWork |
| Kaaka_Muttai | type | Artifact |
| Kaaka_Muttai | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Kaaka_Muttai | hasPublicationDate | "2014"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| En_sømand_går_i_land | type | Film |
| Kaaka_Muttai | hasPublicationDate | "2015"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Kaaka_Muttai | type | Film |

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
