# Triple matching report: 135

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Chimalpopoca | hasSibling | Tlacaelel |
| Chimalpopoca | type | Agent |
| Chimalpopoca | type | Person |
| Tlacaelel | hasChild | Tlilpotoncatzin |
| Tlacaelel | hasSibling | Chimalpopoca |
| Tlacaelel | type | Agent |
| Tlacaelel | type | Person |
| Tlilpotoncatzin | hasParent | Tlacaelel |
| Tlilpotoncatzin | type | Agent |
| Tlilpotoncatzin | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Tlacaelel | hasSibling | moctezuma_i |
| moctezuma_i | hasSibling | Tlacaelel |
| moctezuma_i | type | Agent |
| moctezuma_i | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 14 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.714286 |
| Recall | 1.000000 |
| F1 score | 0.833333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
