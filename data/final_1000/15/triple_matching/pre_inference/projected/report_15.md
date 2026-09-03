# Triple matching report: 15

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Desolation_Angels | hasDirector | Tim_McCann |
| Tim_McCann | hasEducatedAt | State_University_of_New_York_at_Purchase |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Desolation_Angels | type | Film |
| Desolation_Angels | type | NamedIndividual |
| Desolation_Angels | label | "Desolation Angels (1995 film)" |
| State_University_of_New_York_at_Purchase | type | EducationalInstitution |
| State_University_of_New_York_at_Purchase | type | NamedIndividual |
| State_University_of_New_York_at_Purchase | label | "State University of New York at Purchase" |
| Tim_McCann | type | Person |
| Tim_McCann | type | NamedIndividual |
| Tim_McCann | label | "Tim McCann" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
