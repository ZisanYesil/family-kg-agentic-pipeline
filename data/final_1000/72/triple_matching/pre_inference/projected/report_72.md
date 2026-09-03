# Triple matching report: 72

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Pistol_Whipped | hasDirector | Roel_Reiné |
| Roel_Reiné | hasBirthPlace | Dutch |

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
| Dutch | type | Place |
| Dutch | type | NamedIndividual |
| Dutch | label | "Eindhoven" |
| Pistol_Whipped | type | Film |
| Pistol_Whipped | type | NamedIndividual |
| Pistol_Whipped | label | "Pistol Whipped" |
| Roel_Reiné | type | Person |
| Roel_Reiné | type | NamedIndividual |
| Roel_Reiné | label | "Roel Reiné" |

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
