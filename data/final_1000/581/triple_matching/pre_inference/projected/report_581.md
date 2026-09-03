# Triple matching report: 581

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Barbara_Babe_Cushing_Mortimer_Paley | hasSpouse | William_S_Paley |
| William_S_Paley | hasEmployer | Columbia_Broadcasting_System |

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
| Barbara_Babe_Cushing_Mortimer_Paley | type | Person |
| Barbara_Babe_Cushing_Mortimer_Paley | type | NamedIndividual |
| Barbara_Babe_Cushing_Mortimer_Paley | label | "Barbara \"Babe\" Cushing Mortimer Paley" |
| Barbara_Babe_Cushing_Mortimer_Paley | altLabel | "Babe Paley" |
| Columbia_Broadcasting_System | type | Organization |
| Columbia_Broadcasting_System | type | NamedIndividual |
| Columbia_Broadcasting_System | label | "Columbia Broadcasting System" |
| Columbia_Broadcasting_System | altLabel | "CBS" |
| William_S_Paley | type | Person |
| William_S_Paley | type | NamedIndividual |
| William_S_Paley | label | "William Samuel Paley" |
| William_S_Paley | altLabel | "William S. Paley" |

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
