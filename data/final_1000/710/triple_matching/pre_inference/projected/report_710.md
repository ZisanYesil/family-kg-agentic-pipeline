# Triple matching report: 710

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Donald_G_Jackson | hasBurialPlace | Westwood_Village_Memorial_Park_Cemetery |
| The_Roller_Blade_Seven | hasDirector | Donald_G_Jackson |

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
| Donald_G_Jackson | type | Person |
| Donald_G_Jackson | type | NamedIndividual |
| Donald_G_Jackson | label | "Donald G. Jackson" |
| The_Roller_Blade_Seven | type | Film |
| The_Roller_Blade_Seven | type | NamedIndividual |
| The_Roller_Blade_Seven | label | "The Roller Blade Seven" |
| Westwood_Village_Memorial_Park_Cemetery | type | Place |
| Westwood_Village_Memorial_Park_Cemetery | type | NamedIndividual |
| Westwood_Village_Memorial_Park_Cemetery | label | "Westwood Village Memorial Park Cemetery" |

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
