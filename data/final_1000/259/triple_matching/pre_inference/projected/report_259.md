# Triple matching report: 259

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Aatma_Gowravam | hasProducer | D_Madhusudhana_Rao |
| Ajay_Devgn | hasBirthDate | "1969-04-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| D_Madhusudhana_Rao | hasBirthDate | "1917-07-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| Vitti_Dandu | hasProducer | Ajay_Devgn |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Aatma_Gowravam | type | Film |
| Aatma_Gowravam | type | NamedIndividual |
| Aatma_Gowravam | label | "Aatma Gowravam" |
| Ajay_Devgn | type | Person |
| Ajay_Devgn | type | NamedIndividual |
| Ajay_Devgn | label | "Ajay Devgn" |
| D_Madhusudhana_Rao | type | Person |
| D_Madhusudhana_Rao | type | NamedIndividual |
| D_Madhusudhana_Rao | label | "D. Madhusudhana Rao" |
| Vitti_Dandu | type | Film |
| Vitti_Dandu | type | NamedIndividual |
| Vitti_Dandu | label | "Vitti Dandu" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 16 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
