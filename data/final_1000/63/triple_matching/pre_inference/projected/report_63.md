# Triple matching report: 63

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Catholic_University_of_Tachira | hasInception | "1962"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Sri_Dharmaloka_College | hasInception | "1938"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Catholic_University_of_Tachira | type | EducationalInstitution |
| Catholic_University_of_Tachira | type | NamedIndividual |
| Catholic_University_of_Tachira | label | "Catholic University Of Tachira" |
| Catholic_University_of_Tachira | altLabel | "UCAT" |
| Catholic_University_of_Tachira | altLabel | "Universidad Católica del Táchira" |
| Sri_Dharmaloka_College | type | EducationalInstitution |
| Sri_Dharmaloka_College | type | NamedIndividual |
| Sri_Dharmaloka_College | label | "Sri Dharmaloka College" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
