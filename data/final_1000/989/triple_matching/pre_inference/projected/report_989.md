# Triple matching report: 989

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Carlos_Gardel | hasCountry | Argentine |
| Por_una_Cabeza | hasComposer | Carlos_Gardel |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Argentine | type | Country |
| Argentine | type | NamedIndividual |
| Argentine | label | "Argentina" |
| Argentine | altLabel | "Argentine" |
| Carlos_Gardel | hasCountry | country_france |
| Carlos_Gardel | type | Person |
| Carlos_Gardel | type | NamedIndividual |
| Carlos_Gardel | label | "Carlos Gardel" |
| Carlos_Gardel | altLabel | "Carlos Gardel" |
| Por_una_Cabeza | type | MusicalWork |
| Por_una_Cabeza | type | NamedIndividual |
| Por_una_Cabeza | label | "Por una Cabeza" |
| country_france | type | Country |
| country_france | type | NamedIndividual |
| country_france | label | "France" |
| country_france | altLabel | "French" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 18 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.111111 |
| Recall | 1.000000 |
| F1 score | 0.200000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
