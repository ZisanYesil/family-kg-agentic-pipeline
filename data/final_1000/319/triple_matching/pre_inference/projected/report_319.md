# Triple matching report: 319

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Constantia_Eriksdotter | hasParent | Eric_XIV_of_Sweden |
| Eric_XIV_of_Sweden | hasCauseOfDeath | poisoning |

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
| Constantia_Eriksdotter | type | Person |
| Constantia_Eriksdotter | type | NamedIndividual |
| Constantia_Eriksdotter | label | "Constantia Eriksdotter" |
| Eric_XIV_of_Sweden | type | Person |
| Eric_XIV_of_Sweden | type | NamedIndividual |
| Eric_XIV_of_Sweden | label | "Eric XIV of Sweden" |
| poisoning | type | CauseOfDeath |
| poisoning | type | NamedIndividual |
| poisoning | label | "arsenic poisoning" |

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
