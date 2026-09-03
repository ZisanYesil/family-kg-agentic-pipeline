# Triple matching report: 580

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Bjørn_Helland_Hansen | hasEmployer | University_of_Bergen |
| Eigil_Helland_Hansen | hasParent | Bjørn_Helland_Hansen |

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
| Bjørn_Helland_Hansen | type | Person |
| Bjørn_Helland_Hansen | type | NamedIndividual |
| Bjørn_Helland_Hansen | label | "Bjørn Helland-Hansen" |
| Eigil_Helland_Hansen | type | Person |
| Eigil_Helland_Hansen | type | NamedIndividual |
| Eigil_Helland_Hansen | label | "Eigil Helland-Hansen" |
| University_of_Bergen | type | Organization |
| University_of_Bergen | type | NamedIndividual |
| University_of_Bergen | label | "Bergen Museum" |

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
