# Triple matching report: 797

# 1. Matched triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| A_Midnight_Romance | hasProducer | Anita_Stewart |
| A_Midnight_Romance | type | Artifact |
| A_Midnight_Romance | type | CreativeWork |
| Anita_Stewart | hasDeathDate | "1961-05-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| Anita_Stewart | type | Agent |
| Anita_Stewart | type | Person |
| Richard_Widmark | hasDeathDate | "2008-03-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| Richard_Widmark | type | Agent |
| Richard_Widmark | type | Person |
| The_Bedford_Incident | hasProducer | Richard_Widmark |
| The_Bedford_Incident | type | Artifact |
| The_Bedford_Incident | type | CreativeWork |

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
| A_Midnight_Romance | type | Film |
| The_Bedford_Incident | type | Film |

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
