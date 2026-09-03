# Triple matching report: 623

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Dweepa | hasProducer | Soundarya |
| Kalank | hasProducer | Karan_Johar |
| Karan_Johar | hasBirthDate | "1972-05-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Soundarya | hasBirthDate | "1972-07-18"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| Dweepa | hasPublicationDate | "2002"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Dweepa | type | Film |
| Dweepa | type | NamedIndividual |
| Dweepa | label | "Dweepa" |
| Kalank | hasPublicationDate | "2019"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Kalank | type | Film |
| Kalank | type | NamedIndividual |
| Kalank | label | "Kalank" |
| Karan_Johar | type | Person |
| Karan_Johar | type | NamedIndividual |
| Karan_Johar | label | "Karan Kumar Johar" |
| Karan_Johar | altLabel | "Karan Johar" |
| Soundarya | hasDeathDate | "2004-04-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Soundarya | type | Person |
| Soundarya | type | NamedIndividual |
| Soundarya | label | "Soundarya Sathyanarayana" |
| Soundarya | altLabel | "Soundarya" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 21 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 21 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.190476 |
| Recall | 1.000000 |
| F1 score | 0.320000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
