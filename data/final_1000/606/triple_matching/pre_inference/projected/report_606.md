# Triple matching report: 606

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alex_Kramer | hasBirthPlace | Montreal_Quebec |
| Candy | hasComposer | Alex_Kramer |

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
| Alex_Kramer | type | Person |
| Alex_Kramer | type | NamedIndividual |
| Alex_Kramer | label | "Alex Kramer" |
| Alex_Kramer | altLabel | "Alex J. Kramer" |
| Candy | type | MusicalWork |
| Candy | type | NamedIndividual |
| Candy | label | "Candy (1944 song)" |
| Montreal_Quebec | type | Place |
| Montreal_Quebec | type | NamedIndividual |
| Montreal_Quebec | label | "Montreal, Quebec, Canada" |

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
