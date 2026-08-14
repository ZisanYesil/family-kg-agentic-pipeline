# Triple matching report: 10

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Q30 | type | Country |
| Q30 | type | Place |
| Q408 | type | Country |
| Q408 | type | Place |
| Q6787778 | hasCountry | Q408 |
| Q7958642 | hasCountry | Q30 |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Q6787778 | hasInception | "1960"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q6787778 | type | Agent |
| Q6787778 | type | EducationalInstitution |
| Q6787778 | type | Organization |
| Q7958642 | type | Agent |
| Q7958642 | type | EducationalInstitution |
| Q7958642 | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 13 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.461538 |
| Recall | 1.000000 |
| F1 score | 0.631579 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
