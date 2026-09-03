# Triple matching report: 47

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Pre | hasMember | Akiko_Matsuura |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Akiko_Matsuura | hasCountry | Japan |

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Akiko_Matsuura | hasBirthPlace | osaka |
| Akiko_Matsuura | type | Person |
| Akiko_Matsuura | type | NamedIndividual |
| Akiko_Matsuura | label | "Akiko Matsuura" |
| Akiko_Matsuura | altLabel | "Akiko \"Keex\" Matsuura" |
| Japan | type | Country |
| Japan | type | NamedIndividual |
| Japan | label | "Japan" |
| Japan | altLabel | "Japanese" |
| Pre | type | Organization |
| Pre | type | NamedIndividual |
| Pre | label | "Pre (band)" |
| osaka | hasCountry | Japan |
| osaka | type | Place |
| osaka | type | NamedIndividual |
| osaka | label | "Osaka" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 18 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.058824 |
| Recall | 0.500000 |
| F1 score | 0.105263 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
