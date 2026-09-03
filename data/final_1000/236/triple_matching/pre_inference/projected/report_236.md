# Triple matching report: 236

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Don_t_Knock_the_Ox | hasDirector | Tony_Ianzelo |
| Tony_Ianzelo | hasEducatedAt | Ryerson_University |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Don_t_Knock_the_Ox | type | Film |
| Don_t_Knock_the_Ox | type | NamedIndividual |
| Don_t_Knock_the_Ox | label | "Don't Knock the Ox" |
| Ryerson_University | type | EducationalInstitution |
| Ryerson_University | type | NamedIndividual |
| Ryerson_University | label | "Ryerson Polytechnical School" |
| Ryerson_University | altLabel | "Ryerson University" |
| Ryerson_University | altLabel | "Toronto’s Ryerson Polytechnical School" |
| Tony_Ianzelo | type | Person |
| Tony_Ianzelo | type | NamedIndividual |
| Tony_Ianzelo | label | "Tony Ianzelo" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
