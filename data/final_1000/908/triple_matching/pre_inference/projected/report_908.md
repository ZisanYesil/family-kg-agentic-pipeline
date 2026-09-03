# Triple matching report: 908

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Herod_Agrippa | hasParent | Aristobulus_IV |
| Mariamne | hasParent | Herod_Agrippa |

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
| Aristobulus_IV | type | Person |
| Aristobulus_IV | type | NamedIndividual |
| Aristobulus_IV | label | "Aristobulus IV" |
| Herod_Agrippa | type | Person |
| Herod_Agrippa | type | NamedIndividual |
| Herod_Agrippa | label | "Herod Agrippa I" |
| Herod_Agrippa | altLabel | "Herod Agrippa" |
| Mariamne | type | Person |
| Mariamne | type | NamedIndividual |
| Mariamne | label | "Mariamne" |
| Mariamne | altLabel | "Mariamne (daughter of Herod Agrippa)" |

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
