# Triple matching report: 838

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Georges_Lautner | hasParent | Renée_Saint_Cyr |
| My_Other_Husband | hasDirector | Georges_Lautner |

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
| Georges_Lautner | type | Person |
| Georges_Lautner | type | NamedIndividual |
| Georges_Lautner | label | "Georges Lautner" |
| My_Other_Husband | type | Film |
| My_Other_Husband | type | NamedIndividual |
| My_Other_Husband | label | "My Other Husband" |
| Renée_Saint_Cyr | type | Person |
| Renée_Saint_Cyr | type | NamedIndividual |
| Renée_Saint_Cyr | label | "Renée Saint‑Cyr" |

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
