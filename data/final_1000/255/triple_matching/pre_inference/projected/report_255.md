# Triple matching report: 255

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Aud_Egede_Nissen | hasCountry | Norwegian |
| Paul_Richter | hasSpouse | Aud_Egede_Nissen |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Aud_Egede_Nissen | type | Person |
| Aud_Egede_Nissen | type | NamedIndividual |
| Aud_Egede_Nissen | label | "Aud Egede-Nissen" |
| Norwegian | type | Country |
| Norwegian | type | NamedIndividual |
| Norwegian | label | "Norway" |
| Norwegian | altLabel | "Norwegian" |
| Paul_Richter | type | Person |
| Paul_Richter | type | NamedIndividual |
| Paul_Richter | label | "Paul Richter" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
