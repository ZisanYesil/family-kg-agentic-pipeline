# Triple matching report: 825

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Empress_Ren | hasSpouse | Li_Xiong |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Li_Xiong | hasDeathPlace | Chengdu |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Empress_Ren | type | Person |
| Empress_Ren | type | NamedIndividual |
| Empress_Ren | label | "Empress Ren" |
| Li_Xiong | type | Person |
| Li_Xiong | type | NamedIndividual |
| Li_Xiong | label | "Li Xiong" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 8 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.142857 |
| Recall | 0.500000 |
| F1 score | 0.222222 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
