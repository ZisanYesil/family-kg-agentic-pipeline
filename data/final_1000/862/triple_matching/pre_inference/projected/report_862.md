# Triple matching report: 862

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Felix_E_Feist | hasBirthPlace | New_York |
| Guilty_of_Treason | hasDirector | Felix_E_Feist |

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
| Felix_E_Feist | type | Person |
| Felix_E_Feist | type | NamedIndividual |
| Felix_E_Feist | label | "Felix E. Feist" |
| Felix_E_Feist | altLabel | "Felix Ellison Feist" |
| Guilty_of_Treason | type | Film |
| Guilty_of_Treason | type | NamedIndividual |
| Guilty_of_Treason | label | "Guilty of Treason" |
| Guilty_of_Treason | altLabel | "Treason" |
| New_York | type | Place |
| New_York | type | NamedIndividual |
| New_York | label | "New York City" |

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
