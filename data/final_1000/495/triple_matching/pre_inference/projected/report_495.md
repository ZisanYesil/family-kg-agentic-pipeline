# Triple matching report: 495

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Günther_Weißenborn | hasBirthDate | "1911-06-02"^^<http://www.w3.org/2001/XMLSchema#date> |
| Günther_Weißenborn | hasDeathDate | "2001-02-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Pierluigi_Samaritani | hasBirthDate | "1942-09-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Pierluigi_Samaritani | hasDeathDate | "1994-01-05"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Günther_Weißenborn | type | Person |
| Günther_Weißenborn | type | NamedIndividual |
| Günther_Weißenborn | label | "Günther Weißenborn" |
| Pierluigi_Samaritani | type | Person |
| Pierluigi_Samaritani | type | NamedIndividual |
| Pierluigi_Samaritani | label | "Pierluigi Samaritani" |
| Pierluigi_Samaritani | altLabel | "PierLuigi Samaritani" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 11 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.363636 |
| Recall | 1.000000 |
| F1 score | 0.533333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
