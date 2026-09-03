# Triple matching report: 494

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alan_IV_de_Rohan | hasParent | Constance_of_Penthièvre |
| Constance_of_Penthièvre | hasCountry | Breton |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Alan_IV_de_Rohan | type | Person |
| Alan_IV_de_Rohan | type | NamedIndividual |
| Alan_IV_de_Rohan | label | "Alan IV, Viscount of Rohan" |
| Breton | type | Country |
| Breton | type | NamedIndividual |
| Breton | label | "France" |
| Breton | altLabel | "Breton" |
| Constance_of_Penthièvre | type | Person |
| Constance_of_Penthièvre | type | NamedIndividual |
| Constance_of_Penthièvre | label | "Constance of Penthièvre" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
