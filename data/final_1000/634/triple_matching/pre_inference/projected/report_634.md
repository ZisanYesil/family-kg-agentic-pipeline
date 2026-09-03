# Triple matching report: 634

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Amos_Tuck | hasBirthDate | "1810-08-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Amos_Tuck | hasDeathDate | "1879-12-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Hans_Döbrich | hasBirthDate | "1916-03-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| Hans_Döbrich | hasDeathDate | "1984-04-06"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Amos_Tuck | type | Person |
| Amos_Tuck | type | NamedIndividual |
| Amos_Tuck | label | "Amos Tuck" |
| Hans_Döbrich | type | Person |
| Hans_Döbrich | type | NamedIndividual |
| Hans_Döbrich | label | "Hans Döbrich" |

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
