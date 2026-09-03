# Triple matching report: 527

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Eleanor_Roosevelt | type | Agent |
| Eleanor_Roosevelt | type | Person |
| Franklin_Delano_Roosevelt | hasSibling | James_Roosevelt |
| Franklin_Delano_Roosevelt | type | Agent |
| Franklin_Delano_Roosevelt | type | Person |
| James_Roosevelt | hasSibling | Franklin_Delano_Roosevelt |
| James_Roosevelt | type | Agent |
| James_Roosevelt | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Eleanor_Roosevelt | hasSpouse | Franklin_D_Roosevelt |
| Franklin_D_Roosevelt | hasSpouse | Eleanor_Roosevelt |
| Franklin_D_Roosevelt | type | Agent |
| Franklin_D_Roosevelt | type | Person |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Eleanor_Roosevelt | hasSpouse | Franklin_Delano_Roosevelt |
| Franklin_Delano_Roosevelt | hasSpouse | Eleanor_Roosevelt |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 14 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.800000 |
| Recall | 0.666667 |
| F1 score | 0.727273 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
