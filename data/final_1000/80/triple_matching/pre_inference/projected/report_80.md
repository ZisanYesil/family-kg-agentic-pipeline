# Triple matching report: 80

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Devil_s_Playground | hasDirector | Erle_C_Kenton |
| Erle_C_Kenton | hasCauseOfDeath | Parkinson |

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
| Devil_s_Playground | type | Film |
| Devil_s_Playground | type | NamedIndividual |
| Devil_s_Playground | label | "The Devil's Playground (1937 film)" |
| Erle_C_Kenton | type | Person |
| Erle_C_Kenton | type | NamedIndividual |
| Erle_C_Kenton | label | "Erle C. Kenton" |
| Parkinson | type | CauseOfDeath |
| Parkinson | type | NamedIndividual |
| Parkinson | label | "Parkinson's disease" |

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
