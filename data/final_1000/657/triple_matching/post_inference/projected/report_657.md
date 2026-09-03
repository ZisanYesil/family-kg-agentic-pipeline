# Triple matching report: 657

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Michal_Aviad | type | Agent |
| Michal_Aviad | type | Person |
| Tel_Aviv_University | type | Agent |
| Tel_Aviv_University | type | Organization |
| Working_Woman | hasCreator | Michal_Aviad |
| Working_Woman | hasDirector | Michal_Aviad |
| Working_Woman | type | Artifact |
| Working_Woman | type | CreativeWork |
| Working_Woman | type | Film |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Michal_Aviad | hasEmployer | Tel_Aviv_University |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Tel_Aviv_University | type | EducationalInstitution |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 11 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.900000 |
| Recall | 0.900000 |
| F1 score | 0.900000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
