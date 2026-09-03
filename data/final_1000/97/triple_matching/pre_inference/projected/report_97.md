# Triple matching report: 97

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Betty_Lago | hasBirthPlace | Rio_de_Janeiro |
| Eduardo_Conde | hasSpouse | Betty_Lago |

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
| Betty_Lago | type | Person |
| Betty_Lago | type | NamedIndividual |
| Betty_Lago | label | "Betty Lago" |
| Betty_Lago | altLabel | "Elizabeth Lago Netto" |
| Eduardo_Conde | type | Person |
| Eduardo_Conde | type | NamedIndividual |
| Eduardo_Conde | label | "Eduardo Conde" |
| Rio_de_Janeiro | type | Place |
| Rio_de_Janeiro | type | NamedIndividual |
| Rio_de_Janeiro | label | "Rio de Janeiro" |

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
