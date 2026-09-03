# Triple matching report: 664

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Alden_B_Dow | type | Agent |
| Alden_B_Dow | type | Person |
| Case | type | Agent |
| Case | type | EducationalInstitution |
| Case | type | Organization |
| Herbert_Henry_Dow | hasEducatedAt | Case |
| Herbert_Henry_Dow | type | Agent |
| Herbert_Henry_Dow | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alden_B_Dow | hasParent | Herbert_Henry_Dow |
| Herbert_Henry_Dow | hasChild | Alden_B_Dow |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alden_B_Dow | hasChild | Herbert_Henry_Dow |
| Herbert_Henry_Dow | hasParent | Alden_B_Dow |

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
