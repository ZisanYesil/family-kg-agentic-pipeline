# Triple matching report: 656

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| I_Want_You | hasPerformer | Shana |
| Shana | hasBirthPlace | Park_Ridge_Illinois |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| I_Want_You | type | MusicalWork |
| I_Want_You | type | NamedIndividual |
| I_Want_You | label | "I Want You" |
| I_Want_You | altLabel | "I Want You (Shana song)" |
| Park_Ridge_Illinois | type | Place |
| Park_Ridge_Illinois | type | NamedIndividual |
| Park_Ridge_Illinois | label | "Park Ridge, Illinois" |
| Shana | type | Person |
| Shana | type | NamedIndividual |
| Shana | label | "Shana Petrone" |
| Shana | altLabel | "Shana" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
