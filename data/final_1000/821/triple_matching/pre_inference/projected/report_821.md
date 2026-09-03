# Triple matching report: 821

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Harald_III_of_Denmark | hasSpouse | Margareta_Hasbjörnsdatter |
| Margareta_Hasbjörnsdatter | hasBurialPlace | Roskilde_Cathedral |

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
| Harald_III_of_Denmark | type | Person |
| Harald_III_of_Denmark | type | NamedIndividual |
| Harald_III_of_Denmark | label | "Harald III of Denmark" |
| Harald_III_of_Denmark | altLabel | "Harald III" |
| Harald_III_of_Denmark | altLabel | "Harald the Whetstone" |
| Margareta_Hasbjörnsdatter | type | Person |
| Margareta_Hasbjörnsdatter | type | NamedIndividual |
| Margareta_Hasbjörnsdatter | label | "Margareta Hasbjørnsdatter" |
| Margareta_Hasbjörnsdatter | altLabel | "Estrid" |
| Margareta_Hasbjörnsdatter | altLabel | "Margareta Asbjørnsdatter" |
| Roskilde_Cathedral | type | Place |
| Roskilde_Cathedral | type | NamedIndividual |
| Roskilde_Cathedral | label | "Roskilde Cathedral" |

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
