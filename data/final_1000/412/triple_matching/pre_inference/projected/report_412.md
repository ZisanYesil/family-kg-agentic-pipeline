# Triple matching report: 412

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Clarice_Orsini | hasSpouse | Lorenzo_de_Medici |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Lorenzo_de_Medici | hasCountry | Florentine_Republic |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Clarice_Orsini | type | Person |
| Clarice_Orsini | type | NamedIndividual |
| Clarice_Orsini | label | "Clarice Orsini" |
| Lorenzo_de_Medici | hasCountry | italy |
| Lorenzo_de_Medici | type | Person |
| Lorenzo_de_Medici | type | NamedIndividual |
| Lorenzo_de_Medici | label | "Lorenzo de' Medici" |
| italy | type | Country |
| italy | type | NamedIndividual |
| italy | label | "Italy" |
| italy | altLabel | "Italian" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
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
