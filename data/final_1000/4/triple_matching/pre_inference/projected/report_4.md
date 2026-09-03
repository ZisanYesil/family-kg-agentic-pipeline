# Triple matching report: 4

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| John_Middleton_Murry | hasSpouse | Katherine_Mansfield |
| Katherine_Mansfield | hasCauseOfDeath | tuberculosis |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| John_Middleton_Murry | type | Person |
| John_Middleton_Murry | type | NamedIndividual |
| John_Middleton_Murry | label | "John Middleton Murry" |
| Katherine_Mansfield | type | Person |
| Katherine_Mansfield | type | NamedIndividual |
| Katherine_Mansfield | label | "Katherine Mansfield" |
| Katherine_Mansfield | altLabel | "Katherine Mansfield" |
| Katherine_Mansfield | altLabel | "Kathleen Mansfield Murry" |
| tuberculosis | type | CauseOfDeath |
| tuberculosis | type | NamedIndividual |
| tuberculosis | label | "extrapulmonary tuberculosis" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
