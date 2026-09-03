# Triple matching report: 149

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Arabia | hasParent | Sophia |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Sophia | hasCountry | Byzantine_Empire |

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Arabia | type | Person |
| Arabia | type | NamedIndividual |
| Arabia | label | "Arabia" |
| Sophia | type | Person |
| Sophia | type | NamedIndividual |
| Sophia | label | "Sophia" |
| Sophia | altLabel | "Aelia Sophia" |
| Sophia | altLabel | "Sophia (empress)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.111111 |
| Recall | 0.500000 |
| F1 score | 0.181818 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
