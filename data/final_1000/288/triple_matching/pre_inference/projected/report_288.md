# Triple matching report: 288

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Eudokia | hasSpouse | Heraclius |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Heraclius | hasSibling | Theodore |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Eudokia | type | Person |
| Eudokia | type | NamedIndividual |
| Eudokia | label | "Fabia Eudokia" |
| Eudokia | altLabel | "Fabia" |
| Heraclius | type | Person |
| Heraclius | type | NamedIndividual |
| Heraclius | label | "Heraclius" |
| Theodore | hasSibling | Heraclius |
| Theodore | type | Person |
| Theodore | type | NamedIndividual |
| Theodore | label | "Theodore" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
