# Triple matching report: 414

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Hard_Feelings_Loveless | hasCreator | Lorde |
| Hard_Feelings_Loveless | hasPerformer | Lorde |
| Hard_Feelings_Loveless | type | Artifact |
| Hard_Feelings_Loveless | type | CreativeWork |
| Lorde | hasBirthPlace | Takapuna |
| Lorde | type | Agent |
| Lorde | type | Person |
| Takapuna | type | Place |

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
| Hard_Feelings_Loveless | type | MusicalWork |
| Lorde | hasBirthDate | "1996-11-07"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 10 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.800000 |
| Recall | 1.000000 |
| F1 score | 0.888889 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
