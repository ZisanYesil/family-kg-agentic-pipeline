# Triple matching report: 797

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| A_Midnight_Romance | hasProducer | Anita_Stewart |
| Anita_Stewart | hasDeathDate | "1961-05-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| Richard_Widmark | hasDeathDate | "2008-03-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| The_Bedford_Incident | hasProducer | Richard_Widmark |

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
| A_Midnight_Romance | type | Film |
| A_Midnight_Romance | type | NamedIndividual |
| A_Midnight_Romance | label | "A Midnight Romance" |
| Anita_Stewart | type | Person |
| Anita_Stewart | type | NamedIndividual |
| Anita_Stewart | label | "Anita Stewart" |
| Richard_Widmark | type | Person |
| Richard_Widmark | type | NamedIndividual |
| Richard_Widmark | label | "Richard Widmark" |
| The_Bedford_Incident | type | Film |
| The_Bedford_Incident | type | NamedIndividual |
| The_Bedford_Incident | label | "The Bedford Incident" |

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
