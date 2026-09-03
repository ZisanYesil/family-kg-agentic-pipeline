# Triple matching report: 848

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Louise_Tracy | hasSpouse | Spencer_Tracy |
| Louise_Tracy | type | Agent |
| Louise_Tracy | type | Person |
| Spencer_Tracy | hasSpouse | Louise_Tracy |
| Spencer_Tracy | type | Agent |
| Spencer_Tracy | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| American_Academy_of_Dramatic_Arts | type | Agent |
| American_Academy_of_Dramatic_Arts | type | EducationalInstitution |
| American_Academy_of_Dramatic_Arts | type | Organization |
| Spencer_Tracy | hasEducatedAt | American_Academy_of_Dramatic_Arts |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Spencer_Tracy | hasEducatedAt | ripon_college |
| ripon_college | type | Agent |
| ripon_college | type | EducationalInstitution |
| ripon_college | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
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
