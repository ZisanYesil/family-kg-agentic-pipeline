# Triple matching report: 226

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gunhild_of_Wenden | hasCountry | Polish |
| Harald_II_of_Denmark | hasParent | Gunhild_of_Wenden |

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
| Gunhild_of_Wenden | type | Person |
| Gunhild_of_Wenden | type | NamedIndividual |
| Gunhild_of_Wenden | label | "Gunhild of Wenden" |
| Gunhild_of_Wenden | altLabel | "Gunhilda of Wenden" |
| Harald_II_of_Denmark | type | Person |
| Harald_II_of_Denmark | type | NamedIndividual |
| Harald_II_of_Denmark | label | "Harald II of Denmark" |
| Polish | type | Country |
| Polish | type | NamedIndividual |
| Polish | label | "Poland" |
| Polish | altLabel | "Polish" |

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
