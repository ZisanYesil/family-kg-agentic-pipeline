# Triple matching report: 918

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Queen_Gongye | hasSpouse | Injong |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Injong | hasParent | Yejong |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Injong | type | Person |
| Injong | type | NamedIndividual |
| Injong | label | "Injong of Goryeo" |
| Queen_Gongye | type | Person |
| Queen_Gongye | type | NamedIndividual |
| Queen_Gongye | label | "Queen Gongye" |
| Yejong | hasChild | Injong |
| Yejong | type | Person |
| Yejong | type | NamedIndividual |
| Yejong | label | "King Yejong" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
