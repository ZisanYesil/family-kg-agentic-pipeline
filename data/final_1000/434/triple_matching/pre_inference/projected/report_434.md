# Triple matching report: 434

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gerhart_Gerry_Neugebauer | hasSpouse | Marcia_Neugebauer |
| Marcia_Neugebauer | hasBirthPlace | New_York |

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
| Gerhart_Gerry_Neugebauer | type | Person |
| Gerhart_Gerry_Neugebauer | type | NamedIndividual |
| Gerhart_Gerry_Neugebauer | label | "Gerhart \"Gerry\" Neugebauer" |
| Gerhart_Gerry_Neugebauer | altLabel | "Gerry Neugebauer" |
| Marcia_Neugebauer | type | Person |
| Marcia_Neugebauer | type | NamedIndividual |
| Marcia_Neugebauer | label | "Marcia Neugebauer" |
| New_York | type | Place |
| New_York | type | NamedIndividual |
| New_York | label | "New York City" |

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
