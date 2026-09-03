# Triple matching report: 730

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Campbell_Stephen | hasSpouse | Dorothy_Jewson |
| Dorothy_Jewson | hasEducatedAt | Girton_College_Cambridge |

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
| Campbell_Stephen | type | Person |
| Campbell_Stephen | type | NamedIndividual |
| Campbell_Stephen | label | "Campbell Stephen" |
| Campbell_Stephen | altLabel | "Reverend Campbell Stephen" |
| Dorothy_Jewson | type | Person |
| Dorothy_Jewson | type | NamedIndividual |
| Dorothy_Jewson | label | "Dorothy Jewson" |
| Dorothy_Jewson | altLabel | "Dorothea Jewson" |
| Girton_College_Cambridge | type | EducationalInstitution |
| Girton_College_Cambridge | type | NamedIndividual |
| Girton_College_Cambridge | label | "Girton College, Cambridge" |

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
