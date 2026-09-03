# Triple matching report: 604

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Gu_Long | hasEducatedAt | Tamkang_University |
| Gu_Long | type | Agent |
| Gu_Long | type | Person |
| Tamkang_University | type | Agent |
| Tamkang_University | type | EducationalInstitution |
| Tamkang_University | type | Organization |
| The_Return_of_Luk_Siu_fung | hasCreator | Gu_Long |
| The_Return_of_Luk_Siu_fung | type | Artifact |
| The_Return_of_Luk_Siu_fung | type | CreativeWork |

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
| Gu_Long | hasEducatedAt | cheng_kung_senior_high_school |
| cheng_kung_senior_high_school | type | Agent |
| cheng_kung_senior_high_school | type | EducationalInstitution |
| cheng_kung_senior_high_school | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 13 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.692308 |
| Recall | 1.000000 |
| F1 score | 0.818182 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
