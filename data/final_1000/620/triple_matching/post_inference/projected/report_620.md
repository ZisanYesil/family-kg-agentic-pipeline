# Triple matching report: 620

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Canada | type | Country |
| Canada | type | Place |
| Columbia_Montour_Area_Vocational_Technical_School | hasCountry | United_States |
| St_Patrick_s_High_School_Ottawa | hasCountry | Canada |
| United_States | type | Country |
| United_States | type | Place |

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
| Columbia_Montour_Area_Vocational_Technical_School | type | Agent |
| Columbia_Montour_Area_Vocational_Technical_School | type | EducationalInstitution |
| Columbia_Montour_Area_Vocational_Technical_School | type | Organization |
| St_Patrick_s_High_School_Ottawa | type | Agent |
| St_Patrick_s_High_School_Ottawa | type | EducationalInstitution |
| St_Patrick_s_High_School_Ottawa | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 12 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.500000 |
| Recall | 1.000000 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
