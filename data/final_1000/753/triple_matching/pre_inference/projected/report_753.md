# Triple matching report: 753

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jefery_Levy | hasEmployer | University_of_Southern_California |
| Man_of_God | hasDirector | Jefery_Levy |

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
| Jefery_Levy | type | Person |
| Jefery_Levy | type | NamedIndividual |
| Jefery_Levy | label | "Jefery Levy" |
| Man_of_God | type | Film |
| Man_of_God | type | NamedIndividual |
| Man_of_God | label | "Man Of God" |
| University_of_Southern_California | type | EducationalInstitution |
| University_of_Southern_California | type | NamedIndividual |
| University_of_Southern_California | label | "University of Southern California film school" |

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
