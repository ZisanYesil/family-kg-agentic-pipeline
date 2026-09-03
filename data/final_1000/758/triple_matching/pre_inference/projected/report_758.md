# Triple matching report: 758

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Fatima_Maada_Bio | hasSpouse | Julius_Maada_Bio |
| Julius_Maada_Bio | hasEducatedAt | American_University |

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
| American_University | type | EducationalInstitution |
| American_University | type | NamedIndividual |
| American_University | label | "American University" |
| Fatima_Maada_Bio | type | Person |
| Fatima_Maada_Bio | type | NamedIndividual |
| Fatima_Maada_Bio | label | "Fatima Maada Bio" |
| Julius_Maada_Bio | hasEducatedAt | benguema_military_academy |
| Julius_Maada_Bio | type | Person |
| Julius_Maada_Bio | type | NamedIndividual |
| Julius_Maada_Bio | label | "Julius Maada Bio" |
| benguema_military_academy | type | EducationalInstitution |
| benguema_military_academy | type | NamedIndividual |
| benguema_military_academy | label | "Benguema Military Academy" |

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
