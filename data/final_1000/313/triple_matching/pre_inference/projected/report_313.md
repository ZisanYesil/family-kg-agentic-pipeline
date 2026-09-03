# Triple matching report: 313

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| En_sømand_går_i_land | hasPublicationDate | "1954"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Kaaka_Muttai | hasPublicationDate | "2014"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| En_sømand_går_i_land | type | Film |
| En_sømand_går_i_land | type | NamedIndividual |
| En_sømand_går_i_land | label | "En sømand går i land" |
| Kaaka_Muttai | hasPublicationDate | "2015"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Kaaka_Muttai | type | Film |
| Kaaka_Muttai | type | NamedIndividual |
| Kaaka_Muttai | label | "Kaaka Muttai" |

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
