# Triple matching report: 463

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Erle_C_Kenton | hasCauseOfDeath | Parkinson |
| The_Lady_Objects | hasDirector | Erle_C_Kenton |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Erle_C_Kenton | type | Person |
| Erle_C_Kenton | type | NamedIndividual |
| Erle_C_Kenton | label | "Erle C. Kenton" |
| Parkinson | type | CauseOfDeath |
| Parkinson | type | NamedIndividual |
| Parkinson | label | "Parkinson's disease" |
| The_Lady_Objects | type | Film |
| The_Lady_Objects | type | NamedIndividual |
| The_Lady_Objects | label | "The Lady Objects" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
