# Triple matching report: 828

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Colegio_Israelita_de_México | hasInception | "1924"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Colegio_Israelita_de_México | type | Agent |
| Colegio_Israelita_de_México | type | Organization |
| Waldorf_University | hasInception | "1903"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Waldorf_University | type | Agent |
| Waldorf_University | type | Organization |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Colegio_Israelita_de_México | type | EducationalInstitution |
| Waldorf_University | type | EducationalInstitution |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.750000 |
| Recall | 1.000000 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
