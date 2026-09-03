# Triple matching report: 487

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Expedition_Impossible | hasCreator | Mark_Burnett |
| Mark_Burnett | hasCountry | British |

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
| British | type | Country |
| British | type | NamedIndividual |
| British | label | "United Kingdom" |
| British | altLabel | "British" |
| Expedition_Impossible | type | CreativeWork |
| Expedition_Impossible | type | NamedIndividual |
| Expedition_Impossible | label | "Expedition Impossible" |
| Mark_Burnett | type | Person |
| Mark_Burnett | type | NamedIndividual |
| Mark_Burnett | label | "Mark Burnett" |

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
