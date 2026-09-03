# Triple matching report: 526

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Empress_Zhangsun | type | Agent |
| Empress_Zhangsun | type | Person |
| Gaozong | type | Agent |
| Gaozong | type | Person |
| Li_Zhong | type | Agent |
| Li_Zhong | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Empress_Zhangsun | hasChild | Gaozong |
| Gaozong | hasChild | Li_Zhong |
| Gaozong | hasParent | Empress_Zhangsun |
| Li_Zhong | hasParent | Gaozong |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Empress_Zhangsun | hasParent | Gaozong |
| Gaozong | hasChild | Empress_Zhangsun |
| Gaozong | hasParent | Li_Zhong |
| Li_Zhong | hasChild | Gaozong |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 14 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.600000 |
| Recall | 0.600000 |
| F1 score | 0.600000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
