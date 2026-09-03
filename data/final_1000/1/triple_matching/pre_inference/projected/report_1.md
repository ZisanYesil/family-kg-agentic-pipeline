# Triple matching report: 1

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| North_Marion_High_School_Oregon | hasCountry | United_States |
| Seoul_High_School | hasCountry | South_Korea |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| North_Marion_High_School_Oregon | type | EducationalInstitution |
| North_Marion_High_School_Oregon | type | NamedIndividual |
| North_Marion_High_School_Oregon | label | "North Marion High School (Oregon)" |
| North_Marion_High_School_Oregon | altLabel | "North Marion High School" |
| Seoul_High_School | type | EducationalInstitution |
| Seoul_High_School | type | NamedIndividual |
| Seoul_High_School | label | "Seoul High School" |
| South_Korea | type | Country |
| South_Korea | type | NamedIndividual |
| South_Korea | label | "South Korea" |
| South_Korea | altLabel | "Republic of Korea" |
| United_States | type | Country |
| United_States | type | NamedIndividual |
| United_States | label | "United States" |
| United_States | altLabel | "U.S." |
| United_States | altLabel | "U.S.A." |
| United_States | altLabel | "USA" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 19 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.105263 |
| Recall | 1.000000 |
| F1 score | 0.190476 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
