# Triple matching report: 351

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Reach_the_Rock | hasProducer | John_Hughes |

# 2. Unmatched triples

**Total unmatched count: 18**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Butterfly_on_a_Wheel | hasProducer | Pierce_Brosnan |
| John_Hughes_filmmaker | hasBirthDate | "1950-02-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Pierce_Brosnan | hasBirthDate | "1953-05-16"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Butterfly_on_a_Wheel | hasProducer | person_william_morrissey |
| Butterfly_on_a_Wheel | type | Film |
| Butterfly_on_a_Wheel | type | NamedIndividual |
| Butterfly_on_a_Wheel | label | "Butterfly on a Wheel" |
| John_Hughes | hasBirthDate | "1950-02-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| John_Hughes | type | Person |
| John_Hughes | type | NamedIndividual |
| John_Hughes | label | "John Hughes" |
| John_Hughes | altLabel | "John Wilden Hughes Jr." |
| Reach_the_Rock | type | Film |
| Reach_the_Rock | type | NamedIndividual |
| Reach_the_Rock | label | "Reach the Rock" |
| person_william_morrissey | type | Person |
| person_william_morrissey | type | NamedIndividual |
| person_william_morrissey | label | "William Morrissey" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 19 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.062500 |
| Recall | 0.250000 |
| F1 score | 0.100000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
