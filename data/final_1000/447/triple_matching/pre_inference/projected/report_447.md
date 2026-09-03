# Triple matching report: 447

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Dexter_Scott_King | hasParent | Coretta_Scott_King |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Coretta_Scott_King | hasBurialPlace | Georgia |

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Coretta_Scott_King | hasBurialPlace | king_center |
| Coretta_Scott_King | type | Person |
| Coretta_Scott_King | type | NamedIndividual |
| Coretta_Scott_King | label | "Coretta Scott King" |
| Coretta_Scott_King | altLabel | "Coretta Scott King" |
| Dexter_Scott_King | type | Person |
| Dexter_Scott_King | type | NamedIndividual |
| Dexter_Scott_King | label | "Dexter Scott King" |
| Dexter_Scott_King | altLabel | "Dexter King" |
| king_center | type | Place |
| king_center | type | NamedIndividual |
| king_center | label | "King Center" |
| king_center | altLabel | "King Center grounds" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.071429 |
| Recall | 0.500000 |
| F1 score | 0.125000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
