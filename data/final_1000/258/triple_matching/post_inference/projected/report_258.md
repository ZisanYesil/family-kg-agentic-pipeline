# Triple matching report: 258

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Balliol_College | type | Agent |
| Balliol_College | type | EducationalInstitution |
| Balliol_College | type | Organization |
| Margaret_Simey | hasSpouse | Tom_Simey |
| Margaret_Simey | type | Agent |
| Margaret_Simey | type | Person |
| Tom_Simey | hasSpouse | Margaret_Simey |
| Tom_Simey | type | Agent |
| Tom_Simey | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Thomas_Spensley_Simey | hasEducatedAt | Balliol_College |
| Thomas_Spensley_Simey | type | Agent |
| Thomas_Spensley_Simey | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Tom_Simey | hasEducatedAt | Balliol_College |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 13 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.900000 |
| Recall | 0.750000 |
| F1 score | 0.818182 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
