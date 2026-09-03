# Triple matching report: 296

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jan_Nepomucen_Potocki | hasSpouse | Róża_Maria_Wodzicka |
| Stanisław_Antoni_Potocki | hasChild | Jan_Nepomucen_Potocki |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Jan_Nepomucen_Potocki | hasSpouse | maria_szajer |
| Jan_Nepomucen_Potocki | type | Person |
| Jan_Nepomucen_Potocki | type | NamedIndividual |
| Jan_Nepomucen_Potocki | label | "Jan Nepomucen Potocki" |
| Róża_Maria_Wodzicka | type | Person |
| Róża_Maria_Wodzicka | type | NamedIndividual |
| Róża_Maria_Wodzicka | label | "Róża Maria Wodzicka" |
| Stanisław_Antoni_Potocki | type | Person |
| Stanisław_Antoni_Potocki | type | NamedIndividual |
| Stanisław_Antoni_Potocki | label | "Stanisław Antoni Potocki" |
| maria_szajer | type | Person |
| maria_szajer | type | NamedIndividual |
| maria_szajer | label | "Maria Szajer" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
