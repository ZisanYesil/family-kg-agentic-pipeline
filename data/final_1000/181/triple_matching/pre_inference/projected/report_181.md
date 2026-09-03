# Triple matching report: 181

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Dillon_S_Myer | hasBirthDate | "1891-09-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| Dillon_S_Myer | hasDeathDate | "1982-10-21"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jean_de_Bie | hasBirthDate | "1892-05-09"^^<http://www.w3.org/2001/XMLSchema#date> |
| Jean_de_Bie | hasDeathDate | "1961-04-30"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Dillon_S_Myer | type | Person |
| Dillon_S_Myer | type | NamedIndividual |
| Dillon_S_Myer | label | "Dillon S. Myer" |
| Jean_de_Bie | type | Person |
| Jean_de_Bie | type | NamedIndividual |
| Jean_de_Bie | label | "Jean de Bie" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 10 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.400000 |
| Recall | 1.000000 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
