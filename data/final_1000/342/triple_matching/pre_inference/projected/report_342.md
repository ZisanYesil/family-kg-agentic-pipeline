# Triple matching report: 342

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Miriam_Adelson | hasSpouse | Sheldon_Adelson |
| Sheldon_Adelson | hasEmployer | Las_Vegas_Sands |

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
| Las_Vegas_Sands | type | Organization |
| Las_Vegas_Sands | type | NamedIndividual |
| Las_Vegas_Sands | label | "Las Vegas Sands Corporation" |
| Miriam_Adelson | type | Person |
| Miriam_Adelson | type | NamedIndividual |
| Miriam_Adelson | label | "Miriam Adelson" |
| Sheldon_Adelson | type | Person |
| Sheldon_Adelson | type | NamedIndividual |
| Sheldon_Adelson | label | "Sheldon Adelson" |

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
