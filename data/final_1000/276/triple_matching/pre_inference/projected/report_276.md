# Triple matching report: 276

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Nicolae_Ceaușescu | hasCauseOfDeath | firing_squad |
| Zoia_Ceaușescu | hasParent | Nicolae_Ceaușescu |

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
| Nicolae_Ceaușescu | type | Person |
| Nicolae_Ceaușescu | type | NamedIndividual |
| Nicolae_Ceaușescu | label | "Nicolae Ceaușescu" |
| Zoia_Ceaușescu | type | Person |
| Zoia_Ceaușescu | type | NamedIndividual |
| Zoia_Ceaușescu | label | "Zoia Ceaușescu" |
| firing_squad | type | CauseOfDeath |
| firing_squad | type | NamedIndividual |
| firing_squad | label | "execution by firing squad" |

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
