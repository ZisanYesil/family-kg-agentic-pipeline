# Triple matching report: 259

# 1. Matched triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Aatma_Gowravam | hasProducer | D_Madhusudhana_Rao |
| Aatma_Gowravam | type | Artifact |
| Aatma_Gowravam | type | CreativeWork |
| Ajay_Devgn | hasBirthDate | "1969-04-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Ajay_Devgn | type | Agent |
| Ajay_Devgn | type | Person |
| D_Madhusudhana_Rao | hasBirthDate | "1917-07-27"^^<http://www.w3.org/2001/XMLSchema#date> |
| D_Madhusudhana_Rao | type | Agent |
| D_Madhusudhana_Rao | type | Person |
| Vitti_Dandu | hasProducer | Ajay_Devgn |
| Vitti_Dandu | type | Artifact |
| Vitti_Dandu | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Aatma_Gowravam | type | Film |
| Vitti_Dandu | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 14 |
| True positives (matched) | 12 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.857143 |
| Recall | 1.000000 |
| F1 score | 0.923077 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
