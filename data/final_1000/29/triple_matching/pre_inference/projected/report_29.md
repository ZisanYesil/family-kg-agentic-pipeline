# Triple matching report: 29

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Coal_City_Illinois | hasCountry | U_S |
| Lash_Kenar_Nur | hasCountry | Iran |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Coal_City_Illinois | type | Place |
| Coal_City_Illinois | type | NamedIndividual |
| Coal_City_Illinois | label | "Coal City, Illinois" |
| Iran | type | Country |
| Iran | type | NamedIndividual |
| Iran | label | "Iran" |
| Lash_Kenar_Nur | type | Place |
| Lash_Kenar_Nur | type | NamedIndividual |
| Lash_Kenar_Nur | label | "Lash Kenar, Nur" |
| U_S | type | Country |
| U_S | type | NamedIndividual |
| U_S | label | "United States" |
| U_S | altLabel | "America" |
| U_S | altLabel | "U.S." |
| U_S | altLabel | "U.S.A." |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 17 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.117647 |
| Recall | 1.000000 |
| F1 score | 0.210526 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
