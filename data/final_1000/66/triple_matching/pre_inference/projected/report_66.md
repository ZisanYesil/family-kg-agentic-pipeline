# Triple matching report: 66

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| A_South_Sea_Bubble | hasDirector | T_Hayes_Hunter |
| Maury_Dexter | hasCountry | American |
| T_Hayes_Hunter | hasCountry | American |
| The_Young_Animals | hasDirector | Maury_Dexter |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| A_South_Sea_Bubble | type | Film |
| A_South_Sea_Bubble | type | NamedIndividual |
| A_South_Sea_Bubble | label | "A South Sea Bubble" |
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Maury_Dexter | type | Person |
| Maury_Dexter | type | NamedIndividual |
| Maury_Dexter | label | "Maury Dexter" |
| T_Hayes_Hunter | type | Person |
| T_Hayes_Hunter | type | NamedIndividual |
| T_Hayes_Hunter | label | "T. Hayes Hunter" |
| The_Young_Animals | type | Film |
| The_Young_Animals | type | NamedIndividual |
| The_Young_Animals | label | "The Young Animals" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 20 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
