# Triple matching report: 233

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Festival_in_Cannes | hasPublicationDate | "2001"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Petria_s_Wreath | hasPublicationDate | "1980"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Festival_in_Cannes | type | Film |
| Festival_in_Cannes | type | NamedIndividual |
| Festival_in_Cannes | label | "Festival in Cannes" |
| Festival_in_Cannes | altLabel | "Festival in Cannes" |
| Petria_s_Wreath | type | Film |
| Petria_s_Wreath | type | NamedIndividual |
| Petria_s_Wreath | label | "Petria's Wreath" |
| Petria_s_Wreath | altLabel | "Petria's Wreath" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
