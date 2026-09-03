# Triple matching report: 498

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Augustus_Henry_Seward | hasParent | Frances_Adeline_Seward |
| Frances_Adeline_Seward | hasDeathDate | "1865-06-21"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Augustus_Henry_Seward | type | Person |
| Augustus_Henry_Seward | type | NamedIndividual |
| Augustus_Henry_Seward | label | "Augustus Henry Seward" |
| Frances_Adeline_Seward | hasBirthDate | "1805-09-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Frances_Adeline_Seward | type | Person |
| Frances_Adeline_Seward | type | NamedIndividual |
| Frances_Adeline_Seward | label | "Frances Adeline Seward" |
| Frances_Adeline_Seward | altLabel | "Frances Adeline Miller Seward" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
