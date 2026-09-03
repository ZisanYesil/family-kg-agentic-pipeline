# Triple matching report: 309

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Luitgard | hasSpouse | Charlemagne |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Charlemagne | hasCountry | Carolingian_Empire |

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Charlemagne | hasCountry | frankish_country |
| Charlemagne | type | Person |
| Charlemagne | type | NamedIndividual |
| Charlemagne | label | "Charlemagne" |
| Charlemagne | altLabel | "Charles I" |
| Charlemagne | altLabel | "Charles the Great" |
| Luitgard | type | Person |
| Luitgard | type | NamedIndividual |
| Luitgard | label | "Luitgard" |
| Luitgard | altLabel | "Luitgard (Frankish queen)" |
| frankish_country | type | Country |
| frankish_country | type | NamedIndividual |
| frankish_country | label | "Frankish" |
| frankish_country | altLabel | "Frankish" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 16 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.066667 |
| Recall | 0.500000 |
| F1 score | 0.117647 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
