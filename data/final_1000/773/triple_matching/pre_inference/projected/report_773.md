# Triple matching report: 773

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gu_Changwei | hasBirthPlace | Xi_an |
| Love_on_the_Cloud | hasDirector | Gu_Changwei |

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
| Gu_Changwei | type | Person |
| Gu_Changwei | type | NamedIndividual |
| Gu_Changwei | label | "Gu Changwei" |
| Love_on_the_Cloud | type | Film |
| Love_on_the_Cloud | type | NamedIndividual |
| Love_on_the_Cloud | label | "Love on the Cloud" |
| Xi_an | type | Place |
| Xi_an | type | NamedIndividual |
| Xi_an | label | "Xi'an, Shaanxi, People's Republic of China" |

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
