# Triple matching report: 419

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Rachael_Emily_Poole | hasSpouse | Reginald_Lane_Poole |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Reginald_Lane_Poole | hasSibling | Stanley_Lane_Poole |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Rachael_Emily_Poole | type | Person |
| Rachael_Emily_Poole | type | NamedIndividual |
| Rachael_Emily_Poole | label | "Rachael Poole" |
| Rachael_Emily_Poole | altLabel | "Rachael Emily Poole" |
| Reginald_Lane_Poole | type | Person |
| Reginald_Lane_Poole | type | NamedIndividual |
| Reginald_Lane_Poole | label | "Reginald Lane Poole" |
| Reginald_Lane_Poole | altLabel | "Reginald Lane-Poole" |
| Stanley_Lane_Poole | hasSibling | Reginald_Lane_Poole |
| Stanley_Lane_Poole | type | Person |
| Stanley_Lane_Poole | type | NamedIndividual |
| Stanley_Lane_Poole | label | "Stanley Lane-Poole" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
