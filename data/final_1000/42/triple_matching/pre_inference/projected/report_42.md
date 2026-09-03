# Triple matching report: 42

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Joanna_of_Durazzo | hasParent | Maria_of_Calabria |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Maria_of_Calabria | hasDeathPlace | Neapolitan |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Joanna_of_Durazzo | type | Person |
| Joanna_of_Durazzo | type | NamedIndividual |
| Joanna_of_Durazzo | label | "Joanna of Durazzo" |
| Maria_of_Calabria | type | Person |
| Maria_of_Calabria | type | NamedIndividual |
| Maria_of_Calabria | label | "Maria of Calabria" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 8 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.142857 |
| Recall | 0.500000 |
| F1 score | 0.222222 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
