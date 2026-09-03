# Triple matching report: 204

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Gary_Ross | hasCountry | American |
| Seabiscuit_film | hasDirector | Gary_Ross |
| T_Hayes_Hunter | hasCountry | American |
| Warn_London | hasDirector | T_Hayes_Hunter |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Gary_Ross | type | Person |
| Gary_Ross | type | NamedIndividual |
| Gary_Ross | label | "Gary Ross" |
| Seabiscuit_film | type | Film |
| Seabiscuit_film | type | NamedIndividual |
| Seabiscuit_film | label | "Seabiscuit" |
| T_Hayes_Hunter | type | Person |
| T_Hayes_Hunter | type | NamedIndividual |
| T_Hayes_Hunter | label | "T. Hayes Hunter" |
| T_Hayes_Hunter | altLabel | "Thomas Hayes Hunter" |
| Warn_London | type | Film |
| Warn_London | type | NamedIndividual |
| Warn_London | label | "Warn London" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 21 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 21 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.190476 |
| Recall | 1.000000 |
| F1 score | 0.320000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
