# Triple matching report: 241

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| J_Walter_Ruben | hasBurialPlace | Forest_Lawn_Memorial_Park |
| The_Roadhouse_Murder | hasDirector | J_Walter_Ruben |

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
| Forest_Lawn_Memorial_Park | type | Place |
| Forest_Lawn_Memorial_Park | type | NamedIndividual |
| Forest_Lawn_Memorial_Park | label | "Glendale's Forest Lawn Memorial Park Cemetery" |
| J_Walter_Ruben | type | Person |
| J_Walter_Ruben | type | NamedIndividual |
| J_Walter_Ruben | label | "J. Walter Ruben" |
| J_Walter_Ruben | altLabel | "Jacob Walter Ruben" |
| The_Roadhouse_Murder | type | Film |
| The_Roadhouse_Murder | type | NamedIndividual |
| The_Roadhouse_Murder | label | "The Roadhouse Murder" |

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
