# Triple matching report: 542

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Inthasom | hasSibling | Kingkitsarat |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Anurutha | hasParent | Inthasom |

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Anurutha | type | Person |
| Anurutha | type | NamedIndividual |
| Anurutha | label | "Chao Anurutha" |
| Anurutha | altLabel | "Anouruttha" |
| Anurutha | altLabel | "Anurathurat" |
| Anurutha | altLabel | "Anurutha" |
| Inthasom | hasChild | Anurutha |
| Inthasom | type | Person |
| Inthasom | type | NamedIndividual |
| Inthasom | label | "Chao Inthasom" |
| Kingkitsarat | type | Person |
| Kingkitsarat | type | NamedIndividual |
| Kingkitsarat | label | "Kingkitsarat" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.071429 |
| Recall | 0.500000 |
| F1 score | 0.125000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
