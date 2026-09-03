# Triple matching report: 768

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Andrew_Disney | type | Agent |
| Andrew_Disney | type | Person |
| Balls_Out | hasCreator | Andrew_Disney |
| Balls_Out | hasDirector | Andrew_Disney |
| Balls_Out | type | Artifact |
| Balls_Out | type | CreativeWork |
| Balls_Out | type | Film |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Andrew_Disney | hasEducatedAt | Tisch |
| Tisch | type | Agent |
| Tisch | type | EducationalInstitution |
| Tisch | type | Organization |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Andrew_Disney | hasEducatedAt | edu_tisch_school_of_the_arts |
| edu_tisch_school_of_the_arts | type | Agent |
| edu_tisch_school_of_the_arts | type | EducationalInstitution |
| edu_tisch_school_of_the_arts | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 15 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.636364 |
| Recall | 0.636364 |
| F1 score | 0.636364 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
