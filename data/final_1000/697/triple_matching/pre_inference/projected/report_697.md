# Triple matching report: 697

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Theodora_of_Khazaria | hasSibling | Busir |
| Tiberius | hasParent | Theodora_of_Khazaria |

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
| Busir | type | Person |
| Busir | type | NamedIndividual |
| Busir | label | "Busir" |
| Busir | altLabel | "Busir, khagan of the Khazars" |
| Theodora_of_Khazaria | type | Person |
| Theodora_of_Khazaria | type | NamedIndividual |
| Theodora_of_Khazaria | label | "Theodora of Khazaria" |
| Tiberius | type | Person |
| Tiberius | type | NamedIndividual |
| Tiberius | label | "Tiberius" |
| Tiberius | altLabel | "Tiberios" |

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
