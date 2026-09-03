# Triple matching report: 102

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Hurlingham_Reggae_Band | hasMember | Luca_Prodan |
| Luca_Prodan | hasCountry | Italian_Scottish |

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
| Hurlingham_Reggae_Band | type | Organization |
| Hurlingham_Reggae_Band | type | NamedIndividual |
| Hurlingham_Reggae_Band | label | "Hurlingham Reggae Band" |
| Italian_Scottish | type | Country |
| Italian_Scottish | type | NamedIndividual |
| Italian_Scottish | label | "Scotland" |
| Luca_Prodan | hasCountry | italy |
| Luca_Prodan | type | Person |
| Luca_Prodan | type | NamedIndividual |
| Luca_Prodan | label | "Luca Prodan" |
| italy | type | Country |
| italy | type | NamedIndividual |
| italy | label | "Italy" |

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
