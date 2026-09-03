# Triple matching report: 71

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Carlisle_School | hasInception | "1968"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Triam_Udom_Suksa_School | hasInception | "1938"^^<http://www.w3.org/2001/XMLSchema#gYear> |

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
| Carlisle_School | type | EducationalInstitution |
| Carlisle_School | type | NamedIndividual |
| Carlisle_School | label | "Carlisle School" |
| Triam_Udom_Suksa_School | type | EducationalInstitution |
| Triam_Udom_Suksa_School | type | NamedIndividual |
| Triam_Udom_Suksa_School | label | "Triam Udom Suksa School" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 8 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
