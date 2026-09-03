# Triple matching report: 161

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Christopher_Nolan | hasSpouse | Emma_Thomas |
| Jonathan_Nolan | hasSibling | Christopher_Nolan |

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
| Christopher_Nolan | type | Person |
| Christopher_Nolan | type | NamedIndividual |
| Christopher_Nolan | label | "Christopher Nolan" |
| Emma_Thomas | type | Person |
| Emma_Thomas | type | NamedIndividual |
| Emma_Thomas | label | "Emma Thomas" |
| Jonathan_Nolan | type | Person |
| Jonathan_Nolan | type | NamedIndividual |
| Jonathan_Nolan | label | "Jonathan Nolan" |

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
