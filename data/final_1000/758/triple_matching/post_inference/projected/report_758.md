# Triple matching report: 758

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| American_University | type | Agent |
| American_University | type | EducationalInstitution |
| American_University | type | Organization |
| Fatima_Maada_Bio | hasSpouse | Julius_Maada_Bio |
| Fatima_Maada_Bio | type | Agent |
| Fatima_Maada_Bio | type | Person |
| Julius_Maada_Bio | hasEducatedAt | American_University |
| Julius_Maada_Bio | hasSpouse | Fatima_Maada_Bio |
| Julius_Maada_Bio | type | Agent |
| Julius_Maada_Bio | type | Person |

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
| Julius_Maada_Bio | hasEducatedAt | benguema_military_academy |
| benguema_military_academy | type | Agent |
| benguema_military_academy | type | EducationalInstitution |
| benguema_military_academy | type | Organization |

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
