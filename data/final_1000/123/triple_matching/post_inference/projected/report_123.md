# Triple matching report: 123

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Albert_Von_Tilzer | hasBirthDate | "1878-03-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Albert_Von_Tilzer | type | Agent |
| Albert_Von_Tilzer | type | Person |
| Don_t_Take_My_Darling_Boy_Away | hasComposer | Albert_Von_Tilzer |
| Don_t_Take_My_Darling_Boy_Away | hasCreator | Albert_Von_Tilzer |
| Don_t_Take_My_Darling_Boy_Away | type | Artifact |
| Don_t_Take_My_Darling_Boy_Away | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Don_t_Take_My_Darling_Boy_Away | type | MusicalWork |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 8 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.875000 |
| Recall | 1.000000 |
| F1 score | 0.933333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
