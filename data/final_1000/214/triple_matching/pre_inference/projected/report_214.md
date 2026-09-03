# Triple matching report: 214

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Prince_Nikolaus_Wilhelm_of_Nassau | hasParent | Princess_Pauline_of_Württemberg |
| Princess_Pauline_of_Württemberg | hasBirthPlace | Stuttgart |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Prince_Nikolaus_Wilhelm_of_Nassau | type | Person |
| Prince_Nikolaus_Wilhelm_of_Nassau | type | NamedIndividual |
| Prince_Nikolaus_Wilhelm_of_Nassau | label | "Prince Nikolaus Wilhelm of Nassau" |
| Princess_Pauline_of_Württemberg | type | Person |
| Princess_Pauline_of_Württemberg | type | NamedIndividual |
| Princess_Pauline_of_Württemberg | label | "Princess Pauline of Württemberg" |
| Stuttgart | type | Place |
| Stuttgart | type | NamedIndividual |
| Stuttgart | label | "Stuttgart" |
| Stuttgart | altLabel | "Stuttgart, Kingdom of Württemberg" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
