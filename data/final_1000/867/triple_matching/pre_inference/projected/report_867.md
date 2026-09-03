# Triple matching report: 867

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Fast_Car | hasPerformer | Namie_Amuro |
| Namie_Amuro | hasBirthPlace | Naha_Okinawa |

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
| Fast_Car | type | CreativeWork |
| Fast_Car | type | NamedIndividual |
| Fast_Car | label | "Fast Car" |
| Fast_Car | altLabel | "Fast Car (Namie Amuro song)" |
| Naha_Okinawa | type | Place |
| Naha_Okinawa | type | NamedIndividual |
| Naha_Okinawa | label | "Naha, Okinawa, Japan" |
| Namie_Amuro | type | Person |
| Namie_Amuro | type | NamedIndividual |
| Namie_Amuro | label | "Namie Amuro" |
| Namie_Amuro | altLabel | "Amuro" |

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
