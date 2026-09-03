# Triple matching report: 802

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Thep_Kasattri | hasParent | Maha_Chakkraphat |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Maha_Chakkraphat | hasDeathPlace | Ayutthaya |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Maha_Chakkraphat | type | Person |
| Maha_Chakkraphat | type | NamedIndividual |
| Maha_Chakkraphat | label | "Maha Chakkraphat" |
| Maha_Chakkraphat | altLabel | "Maha Chakkraphat" |
| Thep_Kasattri | type | Person |
| Thep_Kasattri | type | NamedIndividual |
| Thep_Kasattri | label | "Thep Kasattri" |
| Thep_Kasattri | altLabel | "Thep Kasat Chao" |
| Thep_Kasattri | altLabel | "Thep Kasattri" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.100000 |
| Recall | 0.500000 |
| F1 score | 0.166667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
