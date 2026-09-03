# Triple matching report: 123

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Albert_Von_Tilzer | hasBirthDate | "1878-03-29"^^<http://www.w3.org/2001/XMLSchema#date> |
| Don_t_Take_My_Darling_Boy_Away | hasComposer | Albert_Von_Tilzer |

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
| Albert_Von_Tilzer | type | Person |
| Albert_Von_Tilzer | type | NamedIndividual |
| Albert_Von_Tilzer | label | "Albert Von Tilzer" |
| Don_t_Take_My_Darling_Boy_Away | type | MusicalWork |
| Don_t_Take_My_Darling_Boy_Away | type | NamedIndividual |
| Don_t_Take_My_Darling_Boy_Away | label | "Don't Take My Darling Boy Away" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 8 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
