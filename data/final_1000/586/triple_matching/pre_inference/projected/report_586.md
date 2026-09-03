# Triple matching report: 586

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Curtis_Bernhardt | hasBurialPlace | Forest_Lawn_Memorial_Park |
| Juke_Girl | hasDirector | Curtis_Bernhardt |

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
| Curtis_Bernhardt | type | Person |
| Curtis_Bernhardt | type | NamedIndividual |
| Curtis_Bernhardt | label | "Curtis Bernhardt" |
| Forest_Lawn_Memorial_Park | type | Place |
| Forest_Lawn_Memorial_Park | type | NamedIndividual |
| Forest_Lawn_Memorial_Park | label | "Glendale's Forest Lawn Memorial Park Cemetery" |
| Forest_Lawn_Memorial_Park | altLabel | "Forest Lawn Memorial Park Cemetery" |
| Juke_Girl | type | Film |
| Juke_Girl | type | NamedIndividual |
| Juke_Girl | label | "Juke Girl" |

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
