# Triple matching report: 686

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Adam_Yauch | hasCauseOfDeath | cancer |
| Awesome_I_Fuckin_Shot_That | hasDirector | Adam_Yauch |

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
| Adam_Yauch | type | Person |
| Adam_Yauch | type | NamedIndividual |
| Adam_Yauch | label | "Adam Yauch" |
| Adam_Yauch | altLabel | "Adam Nathaniel Yauch" |
| Awesome_I_Fuckin_Shot_That | type | Film |
| Awesome_I_Fuckin_Shot_That | type | NamedIndividual |
| Awesome_I_Fuckin_Shot_That | label | "Awesome; I Fuckin' Shot That!" |
| cancer | type | CauseOfDeath |
| cancer | type | NamedIndividual |
| cancer | label | "parotid cancer" |

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
