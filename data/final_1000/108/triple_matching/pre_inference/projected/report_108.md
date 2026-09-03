# Triple matching report: 108

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Edwin_August | hasBurialPlace | Valhalla_Memorial_Park_Cemetery |
| The_Yellow_Passport | hasDirector | Edwin_August |

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
| Edwin_August | type | Person |
| Edwin_August | type | NamedIndividual |
| Edwin_August | label | "Edwin August" |
| Edwin_August | altLabel | "Edwin August Phillip von der Butz" |
| The_Yellow_Passport | type | Film |
| The_Yellow_Passport | type | NamedIndividual |
| The_Yellow_Passport | label | "The Yellow Passport" |
| Valhalla_Memorial_Park_Cemetery | type | Place |
| Valhalla_Memorial_Park_Cemetery | type | NamedIndividual |
| Valhalla_Memorial_Park_Cemetery | label | "Valhalla Memorial Park Cemetery" |

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
