# Triple matching report: 633

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Chaohu_University | hasCountry | Chinese |
| Chinese | type | Country |
| Chinese | type | Place |
| Shanghai_Normal_University | hasCountry | Chinese |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Chaohu_University | type | Agent |
| Chaohu_University | type | EducationalInstitution |
| Chaohu_University | type | Organization |
| Shanghai_Normal_University | type | Agent |
| Shanghai_Normal_University | type | EducationalInstitution |
| Shanghai_Normal_University | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 10 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.400000 |
| Recall | 1.000000 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
