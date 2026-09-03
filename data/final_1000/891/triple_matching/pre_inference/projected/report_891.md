# Triple matching report: 891

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Elías_Sapag | hasBirthPlace | Mayrouba |
| Jorge_Sapag | hasParent | Elías_Sapag |

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
| Elías_Sapag | type | Person |
| Elías_Sapag | type | NamedIndividual |
| Elías_Sapag | label | "Elías Canaán Sapag" |
| Elías_Sapag | altLabel | "Elías Sapag" |
| Jorge_Sapag | type | Person |
| Jorge_Sapag | type | NamedIndividual |
| Jorge_Sapag | label | "Jorge Augusto Sapag" |
| Jorge_Sapag | altLabel | "Jorge Sapag" |
| Mayrouba | type | Place |
| Mayrouba | type | NamedIndividual |
| Mayrouba | label | "Mayrouba, Lebanon" |
| Mayrouba | altLabel | "Mayrouba" |

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
