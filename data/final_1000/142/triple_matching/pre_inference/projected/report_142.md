# Triple matching report: 142

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Macrianus_Major | hasDeathPlace | Thrace |
| Macrianus_Minor | hasParent | Macrianus_Major |

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
| Macrianus_Major | type | Person |
| Macrianus_Major | type | NamedIndividual |
| Macrianus_Major | label | "Fulvius Macrianus" |
| Macrianus_Major | altLabel | "Macrianus Major" |
| Macrianus_Minor | type | Person |
| Macrianus_Minor | type | NamedIndividual |
| Macrianus_Minor | label | "Titus Fulvius Iunius Macrianus" |
| Macrianus_Minor | altLabel | "Macrianus Minor" |
| Thrace | type | Place |
| Thrace | type | NamedIndividual |
| Thrace | label | "Thrace" |

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
