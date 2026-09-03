# Triple matching report: 659

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| A_Bullet_Is_Waiting | hasDirector | John_Farrow |
| John_Farrow | hasSpouse | Maureen_O_Sullivan |

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
| A_Bullet_Is_Waiting | type | Film |
| A_Bullet_Is_Waiting | type | NamedIndividual |
| A_Bullet_Is_Waiting | label | "A Bullet Is Waiting" |
| John_Farrow | type | Person |
| John_Farrow | type | NamedIndividual |
| John_Farrow | label | "John Farrow" |
| Maureen_O_Sullivan | type | Person |
| Maureen_O_Sullivan | type | NamedIndividual |
| Maureen_O_Sullivan | label | "Maureen O'Sullivan" |

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
