# Triple matching report: 171

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Timothy_West | hasSpouse | Prunella_Scales |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Lockwood_West | hasChild | Timothy_West |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Lockwood_West | type | Person |
| Lockwood_West | type | NamedIndividual |
| Lockwood_West | label | "Lockwood West" |
| Lockwood_West | altLabel | "Harry Lockwood West" |
| Prunella_Scales | type | Person |
| Prunella_Scales | type | NamedIndividual |
| Prunella_Scales | label | "Prunella Scales" |
| Timothy_West | hasParent | Lockwood_West |
| Timothy_West | type | Person |
| Timothy_West | type | NamedIndividual |
| Timothy_West | label | "Timothy West" |
| Timothy_West | altLabel | "Timothy Lancaster West" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
