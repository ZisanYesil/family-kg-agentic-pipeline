# Triple matching report: 623

# 1. Matched triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Dweepa | hasProducer | Soundarya |
| Dweepa | type | Artifact |
| Dweepa | type | CreativeWork |
| Kalank | hasProducer | Karan_Johar |
| Kalank | type | Artifact |
| Kalank | type | CreativeWork |
| Karan_Johar | hasBirthDate | "1972-05-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Karan_Johar | type | Agent |
| Karan_Johar | type | Person |
| Soundarya | hasBirthDate | "1972-07-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Soundarya | type | Agent |
| Soundarya | type | Person |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Dweepa | hasPublicationDate | "2002"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Dweepa | type | Film |
| Kalank | hasPublicationDate | "2019"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Kalank | type | Film |
| Soundarya | hasDeathDate | "2004-04-17"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 17 |
| True positives (matched) | 12 |
| False positives (extracted-only) | 5 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.705882 |
| Recall | 1.000000 |
| F1 score | 0.827586 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
