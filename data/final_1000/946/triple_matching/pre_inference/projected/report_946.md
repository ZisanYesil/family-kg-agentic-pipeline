# Triple matching report: 946

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Alice_O_Fredericks | hasDeathDate | "1968-02-18"^^<http://www.w3.org/2001/XMLSchema#date> |
| Crime_Against_Joe | hasDirector | Lee_Sholem |
| Lee_Sholem | hasDeathDate | "2000-08-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Vagabonderne_på_Bakkegården | hasDirector | Alice_O_Fredericks |

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
| Alice_O_Fredericks | type | Person |
| Alice_O_Fredericks | type | NamedIndividual |
| Alice_O_Fredericks | label | "Alice O'Fredericks" |
| Crime_Against_Joe | type | Film |
| Crime_Against_Joe | type | NamedIndividual |
| Crime_Against_Joe | label | "Crime Against Joe" |
| Lee_Sholem | type | Person |
| Lee_Sholem | type | NamedIndividual |
| Lee_Sholem | label | "Lee Sholem" |
| Vagabonderne_på_Bakkegården | type | Film |
| Vagabonderne_på_Bakkegården | type | NamedIndividual |
| Vagabonderne_på_Bakkegården | label | "Vagabonderne på Bakkegården" |

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
