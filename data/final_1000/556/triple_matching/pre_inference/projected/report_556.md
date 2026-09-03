# Triple matching report: 556

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Kosobokovo | hasCountry | Russia |
| Pavlovka_Uglovsky_District_Altai_Krai | hasCountry | Russia |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Kosobokovo | type | Place |
| Kosobokovo | type | NamedIndividual |
| Kosobokovo | label | "Kosobokovo" |
| Pavlovka_Uglovsky_District_Altai_Krai | type | Place |
| Pavlovka_Uglovsky_District_Altai_Krai | type | NamedIndividual |
| Pavlovka_Uglovsky_District_Altai_Krai | label | "Pavlovka, Uglovsky District, Altai Krai" |
| Russia | type | Country |
| Russia | type | NamedIndividual |
| Russia | label | "Russia" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
