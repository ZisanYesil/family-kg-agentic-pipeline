# Triple matching report: 351

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Butterfly_on_a_Wheel | type | Artifact |
| Butterfly_on_a_Wheel | type | CreativeWork |
| John_Hughes | type | Agent |
| Reach_the_Rock | hasProducer | John_Hughes |
| Reach_the_Rock | type | Artifact |
| Reach_the_Rock | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Butterfly_on_a_Wheel | hasProducer | Pierce_Brosnan |
| John_Hughes_filmmaker | hasBirthDate | "1950-02-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| John_Hughes_filmmaker | type | Agent |
| John_Hughes_filmmaker | type | Person |
| Pierce_Brosnan | hasBirthDate | "1953-05-16"^^<http://www.w3.org/2001/XMLSchema#date> |
| Pierce_Brosnan | type | Agent |
| Pierce_Brosnan | type | Person |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Butterfly_on_a_Wheel | hasProducer | person_william_morrissey |
| Butterfly_on_a_Wheel | type | Film |
| John_Hughes | hasBirthDate | "1950-02-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| John_Hughes | type | Person |
| Reach_the_Rock | type | Film |
| person_william_morrissey | type | Agent |
| person_william_morrissey | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 13 |
| Union triples in scope | 20 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 7 |
| Precision | 0.461538 |
| Recall | 0.461538 |
| F1 score | 0.461538 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
