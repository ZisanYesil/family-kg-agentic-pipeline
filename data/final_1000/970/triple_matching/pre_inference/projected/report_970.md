# Triple matching report: 970

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gary_Entin | hasBirthPlace | Miami_Florida |
| Geography_Club | hasDirector | Gary_Entin |

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
| Gary_Entin | type | Person |
| Gary_Entin | type | NamedIndividual |
| Gary_Entin | label | "Gary Entin" |
| Geography_Club | type | Film |
| Geography_Club | type | NamedIndividual |
| Geography_Club | label | "Geography Club" |
| Miami_Florida | type | Place |
| Miami_Florida | type | NamedIndividual |
| Miami_Florida | label | "Miami, Florida" |

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
