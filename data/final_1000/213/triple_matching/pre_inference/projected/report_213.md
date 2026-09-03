# Triple matching report: 213

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Dear_Brat | hasPublicationDate | "1951"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Eleven_Pairs_of_Boots | hasPublicationDate | "1954"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Dear_Brat | type | Film |
| Dear_Brat | type | NamedIndividual |
| Dear_Brat | label | "Dear Brat" |
| Eleven_Pairs_of_Boots | type | Film |
| Eleven_Pairs_of_Boots | type | NamedIndividual |
| Eleven_Pairs_of_Boots | label | "Eleven Pairs of Boots" |
| Eleven_Pairs_of_Boots | altLabel | "Once pares de botas" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
