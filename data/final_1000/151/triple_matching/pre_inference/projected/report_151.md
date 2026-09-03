# Triple matching report: 151

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jimmy_Wales | hasBirthPlace | Huntsville_Alabama |
| WikiTribune | hasFounder | Jimmy_Wales |

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
| Huntsville_Alabama | type | Place |
| Huntsville_Alabama | type | NamedIndividual |
| Huntsville_Alabama | label | "Huntsville, Alabama" |
| Jimmy_Wales | type | Person |
| Jimmy_Wales | type | NamedIndividual |
| Jimmy_Wales | label | "Jimmy Wales" |
| WikiTribune | type | Organization |
| WikiTribune | type | NamedIndividual |
| WikiTribune | label | "WikiTribune" |

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
