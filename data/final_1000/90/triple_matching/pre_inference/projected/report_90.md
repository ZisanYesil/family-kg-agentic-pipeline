# Triple matching report: 90

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Gustav_Lindau | hasBirthDate | "1866-05-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Gustav_Lindau | hasDeathDate | "1923-10-10"^^<http://www.w3.org/2001/XMLSchema#date> |
| Nafija_Sarajlić | hasBirthDate | "1893-10-03"^^<http://www.w3.org/2001/XMLSchema#date> |
| Nafija_Sarajlić | hasDeathDate | "1970-01-15"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Gustav_Lindau | type | Person |
| Gustav_Lindau | type | NamedIndividual |
| Gustav_Lindau | label | "Gustav Lindau" |
| Gustav_Lindau | altLabel | "Gustav Lindau" |
| Nafija_Sarajlić | type | Person |
| Nafija_Sarajlić | type | NamedIndividual |
| Nafija_Sarajlić | label | "Nafija Sarajlić" |
| Nafija_Sarajlić | altLabel | "Nafija Sarajlić" |
| Nafija_Sarajlić | altLabel | "née Hadžikarić" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 13 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.307692 |
| Recall | 1.000000 |
| F1 score | 0.470588 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
