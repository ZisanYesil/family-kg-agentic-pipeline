# Triple matching report: 883

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Paul_Bern | hasSpouse | Jean_Harlow |
| The_Dressmaker_from_Paris | hasDirector | Paul_Bern |

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
| Jean_Harlow | type | Person |
| Jean_Harlow | type | NamedIndividual |
| Jean_Harlow | label | "Jean Harlow" |
| Paul_Bern | type | Person |
| Paul_Bern | type | NamedIndividual |
| Paul_Bern | label | "Paul Bern" |
| The_Dressmaker_from_Paris | type | Film |
| The_Dressmaker_from_Paris | type | NamedIndividual |
| The_Dressmaker_from_Paris | label | "The Dressmaker from Paris" |

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
