# Triple matching report: 125

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| High_Courses_for_Scriptwriters_and_Film_Directors | type | Agent |
| High_Courses_for_Scriptwriters_and_Film_Directors | type | Organization |
| Rolan_Bykov | type | Agent |
| Rolan_Bykov | type | Person |
| Summer_Is_Over | hasCreator | Rolan_Bykov |
| Summer_Is_Over | hasDirector | Rolan_Bykov |
| Summer_Is_Over | type | Artifact |
| Summer_Is_Over | type | CreativeWork |
| Summer_Is_Over | type | Film |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Rolan_Bykov | hasEmployer | High_Courses_for_Scriptwriters_and_Film_Directors |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| High_Courses_for_Scriptwriters_and_Film_Directors | type | EducationalInstitution |
| Rolan_Bykov | hasEducatedAt | High_Courses_for_Scriptwriters_and_Film_Directors |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 12 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.818182 |
| Recall | 0.900000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
