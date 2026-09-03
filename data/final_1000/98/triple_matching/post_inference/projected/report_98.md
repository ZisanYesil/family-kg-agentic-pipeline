# Triple matching report: 98

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Francis_Williams_Rockwell | type | Agent |
| Francis_Williams_Rockwell | type | Person |
| Julius_Rockwell | hasEducatedAt | Yale |
| Julius_Rockwell | type | Agent |
| Julius_Rockwell | type | Person |
| Yale | type | Agent |
| Yale | type | EducationalInstitution |
| Yale | type | Organization |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Francis_Williams_Rockwell | hasParent | Julius_Rockwell |
| Julius_Rockwell | hasChild | Francis_Williams_Rockwell |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Francis_Williams_Rockwell | hasChild | Julius_Rockwell |
| Julius_Rockwell | hasParent | Francis_Williams_Rockwell |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 12 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.800000 |
| Recall | 0.800000 |
| F1 score | 0.800000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
