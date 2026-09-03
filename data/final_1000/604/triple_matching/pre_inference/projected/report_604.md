# Triple matching report: 604

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gu_Long | hasEducatedAt | Tamkang_University |
| The_Return_of_Luk_Siu_fung | hasCreator | Gu_Long |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Gu_Long | hasEducatedAt | cheng_kung_senior_high_school |
| Gu_Long | type | Person |
| Gu_Long | type | NamedIndividual |
| Gu_Long | label | "Gu Long" |
| Tamkang_University | type | EducationalInstitution |
| Tamkang_University | type | NamedIndividual |
| Tamkang_University | label | "Tamkang University" |
| The_Return_of_Luk_Siu_fung | type | CreativeWork |
| The_Return_of_Luk_Siu_fung | type | NamedIndividual |
| The_Return_of_Luk_Siu_fung | label | "The Return of Luk Siu-fung" |
| cheng_kung_senior_high_school | type | EducationalInstitution |
| cheng_kung_senior_high_school | type | NamedIndividual |
| cheng_kung_senior_high_school | label | "Cheng Kung Senior High School" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
