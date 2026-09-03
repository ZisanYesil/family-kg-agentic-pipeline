# Triple matching report: 125

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Summer_Is_Over | hasDirector | Rolan_Bykov |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Rolan_Bykov | hasEmployer | High_Courses_for_Scriptwriters_and_Film_Directors |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| High_Courses_for_Scriptwriters_and_Film_Directors | type | EducationalInstitution |
| High_Courses_for_Scriptwriters_and_Film_Directors | type | NamedIndividual |
| High_Courses_for_Scriptwriters_and_Film_Directors | label | "High Courses for Scriptwriters and Film Directors" |
| Rolan_Bykov | hasEducatedAt | High_Courses_for_Scriptwriters_and_Film_Directors |
| Rolan_Bykov | type | Person |
| Rolan_Bykov | type | NamedIndividual |
| Rolan_Bykov | label | "Rolan Bykov" |
| Rolan_Bykov | altLabel | "Rolan Antonovich Bykov" |
| Summer_Is_Over | type | Film |
| Summer_Is_Over | type | NamedIndividual |
| Summer_Is_Over | label | "Summer Is Over" |
| Summer_Is_Over | altLabel | "Summer Is Over (film)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
