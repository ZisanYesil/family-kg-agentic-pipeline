# Triple matching report: 721

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| John_II_The_Babymaker_Duke_of_Cleves | hasSpouse | Mathilde_of_Hesse |
| Mathilde_of_Hesse | hasDeathPlace | Cologne |

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
| Cologne | type | Place |
| Cologne | type | NamedIndividual |
| Cologne | label | "Cologne" |
| John_II_The_Babymaker_Duke_of_Cleves | type | Person |
| John_II_The_Babymaker_Duke_of_Cleves | type | NamedIndividual |
| John_II_The_Babymaker_Duke_of_Cleves | label | "John II, Duke of Cleves" |
| Mathilde_of_Hesse | type | Person |
| Mathilde_of_Hesse | type | NamedIndividual |
| Mathilde_of_Hesse | label | "Mathilde of Hesse" |

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
