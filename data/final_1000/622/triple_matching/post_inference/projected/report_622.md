# Triple matching report: 622

# 1. Matched triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| CRD | hasCreator | Kranti_Kanade |
| CRD | hasDirector | Kranti_Kanade |
| CRD | type | Artifact |
| CRD | type | CreativeWork |
| CRD | type | Film |
| Kranti_Kanade | hasEducatedAt | UCLA |
| Kranti_Kanade | type | Agent |
| Kranti_Kanade | type | Person |
| UCLA | type | Agent |
| UCLA | type | EducationalInstitution |
| UCLA | type | Organization |

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
| Kranti_Kanade | hasEducatedAt | edu_ftii |
| edu_ftii | type | Agent |
| edu_ftii | type | EducationalInstitution |
| edu_ftii | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 15 |
| True positives (matched) | 11 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.733333 |
| Recall | 1.000000 |
| F1 score | 0.846154 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
