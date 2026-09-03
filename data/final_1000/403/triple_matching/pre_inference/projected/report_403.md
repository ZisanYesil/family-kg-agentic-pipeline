# Triple matching report: 403

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Ash_Koosha | hasCountry | British_Iranian |

# 2. Unmatched triples

**Total unmatched count: 18**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Take_It_Easy_Hospital | hasMember | Ash_Koosha |

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| Ash_Koosha | hasCountry | united_kingdom |
| Ash_Koosha | type | Person |
| Ash_Koosha | type | NamedIndividual |
| Ash_Koosha | label | "Ashkan Kooshanejad" |
| Ash_Koosha | altLabel | "Ash Koosha" |
| British_Iranian | type | Country |
| British_Iranian | type | NamedIndividual |
| British_Iranian | label | "Iran" |
| British_Iranian | altLabel | "Iranian" |
| Take_It_Easy_Hospital | hasFounder | Ash_Koosha |
| Take_It_Easy_Hospital | type | Organization |
| Take_It_Easy_Hospital | type | NamedIndividual |
| Take_It_Easy_Hospital | label | "Take It Easy Hospital" |
| united_kingdom | type | Country |
| united_kingdom | type | NamedIndividual |
| united_kingdom | label | "United Kingdom" |
| united_kingdom | altLabel | "British" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 19 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.055556 |
| Recall | 0.500000 |
| F1 score | 0.100000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
