# Triple matching report: 315

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Georges_Franju | hasBirthPlace | Fougères |
| Thomas_the_Impostor | hasDirector | Georges_Franju |

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
| Fougères | type | Place |
| Fougères | type | NamedIndividual |
| Fougères | label | "Fougères, Ille-et-Vilaine" |
| Georges_Franju | type | Person |
| Georges_Franju | type | NamedIndividual |
| Georges_Franju | label | "Georges Franju" |
| Thomas_the_Impostor | type | Film |
| Thomas_the_Impostor | type | NamedIndividual |
| Thomas_the_Impostor | label | "Thomas the Impostor" |

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
