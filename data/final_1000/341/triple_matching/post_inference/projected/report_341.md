# Triple matching report: 341

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Bruce_Herschensohn | type | Agent |
| Bruce_Herschensohn | type | Person |
| John_F_Kennedy_Years_of_Lightning_Day_of_Drums | hasCreator | Bruce_Herschensohn |
| John_F_Kennedy_Years_of_Lightning_Day_of_Drums | hasDirector | Bruce_Herschensohn |
| John_F_Kennedy_Years_of_Lightning_Day_of_Drums | type | Artifact |
| John_F_Kennedy_Years_of_Lightning_Day_of_Drums | type | CreativeWork |
| John_F_Kennedy_Years_of_Lightning_Day_of_Drums | type | Film |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Bruce_Herschensohn | hasEmployer | Harvard |
| Harvard | type | Agent |
| Harvard | type | Organization |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Bruce_Herschensohn | hasEmployer | org_pepperdine_university_school_of_public_policy |
| org_pepperdine_university_school_of_public_policy | type | Agent |
| org_pepperdine_university_school_of_public_policy | type | EducationalInstitution |
| org_pepperdine_university_school_of_public_policy | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 14 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.636364 |
| Recall | 0.700000 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
