# Triple matching report: 657

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Working_Woman | hasDirector | Michal_Aviad |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Michal_Aviad | hasEmployer | Tel_Aviv_University |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Michal_Aviad | type | Person |
| Michal_Aviad | type | NamedIndividual |
| Michal_Aviad | label | "Michal Aviad" |
| Tel_Aviv_University | type | EducationalInstitution |
| Tel_Aviv_University | type | NamedIndividual |
| Tel_Aviv_University | label | "Tel Aviv University" |
| Working_Woman | type | Film |
| Working_Woman | type | NamedIndividual |
| Working_Woman | label | "Working Woman" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.100000 |
| Recall | 0.500000 |
| F1 score | 0.166667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
