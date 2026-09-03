# Triple matching report: 26

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Lasse_Dahlquist | hasCauseOfDeath | laryngeal_cancer |
| Oh_boy_oh_boy_oh_boy | hasPerformer | Lasse_Dahlquist |

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
| Lasse_Dahlquist | type | Person |
| Lasse_Dahlquist | type | NamedIndividual |
| Lasse_Dahlquist | label | "Lasse Dahlquist" |
| Oh_boy_oh_boy_oh_boy | type | MusicalWork |
| Oh_boy_oh_boy_oh_boy | type | NamedIndividual |
| Oh_boy_oh_boy_oh_boy | label | "Oh boy, oh boy, oh boy!" |
| laryngeal_cancer | type | CauseOfDeath |
| laryngeal_cancer | type | NamedIndividual |
| laryngeal_cancer | label | "laryngeal cancer" |

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
