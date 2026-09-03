# Triple matching report: 414

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Hard_Feelings_Loveless | hasPerformer | Lorde |
| Lorde | hasBirthPlace | Takapuna |

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
| Hard_Feelings_Loveless | type | MusicalWork |
| Hard_Feelings_Loveless | type | NamedIndividual |
| Hard_Feelings_Loveless | label | "Hard Feelings/Loveless" |
| Lorde | hasBirthDate | "1996-11-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Lorde | type | Person |
| Lorde | type | NamedIndividual |
| Lorde | label | "Lorde" |
| Lorde | altLabel | "Ella Marija Lani Yelich-O'Connor" |
| Takapuna | type | Place |
| Takapuna | type | NamedIndividual |
| Takapuna | label | "Takapuna" |
| Takapuna | altLabel | "Auckland suburb of Takapuna" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.142857 |
| Recall | 1.000000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
