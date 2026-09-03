# Triple matching report: 477

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Stands_for_Decibels | hasPublicationDate | "1981"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Pleasure_Victim | hasPublicationDate | "1983"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Pleasure_Victim | hasPublicationDate | "1982"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Pleasure_Victim | type | CreativeWork |
| Pleasure_Victim | type | NamedIndividual |
| Pleasure_Victim | label | "Pleasure Victim" |
| Stands_for_Decibels | type | CreativeWork |
| Stands_for_Decibels | type | NamedIndividual |
| Stands_for_Decibels | label | "Stands for Decibels" |

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
