# Triple matching report: 740

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Million_Dollar_Mile | hasPresenter | Tim_Tebow |
| Tim_Tebow | hasAwardReceived | Heisman_Trophy |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Heisman_Trophy | type | Award |
| Heisman_Trophy | type | NamedIndividual |
| Heisman_Trophy | label | "Heisman Trophy" |
| Heisman_Trophy | altLabel | "Heisman Trophy" |
| Million_Dollar_Mile | type | CreativeWork |
| Million_Dollar_Mile | type | NamedIndividual |
| Million_Dollar_Mile | label | "Million Dollar Mile" |
| Million_Dollar_Mile | altLabel | "Million Dollar Mile" |
| Tim_Tebow | hasBirthDate | "1987-08-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Tim_Tebow | type | Person |
| Tim_Tebow | type | NamedIndividual |
| Tim_Tebow | label | "Tim Tebow" |
| Tim_Tebow | altLabel | "Tim Tebow" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
