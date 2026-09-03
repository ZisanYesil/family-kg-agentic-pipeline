# Triple matching report: 190

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| San_Clemente_Brescia | hasCountry | Italy |
| Santi_Apostoli_Naples | hasCountry | Italy |

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
| Italy | type | Country |
| Italy | type | NamedIndividual |
| Italy | label | "Italy" |
| San_Clemente_Brescia | type | Place |
| San_Clemente_Brescia | type | NamedIndividual |
| San_Clemente_Brescia | label | "San Clemente, Brescia" |
| Santi_Apostoli_Naples | type | Place |
| Santi_Apostoli_Naples | type | NamedIndividual |
| Santi_Apostoli_Naples | label | "Santi Apostoli, Naples" |

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
