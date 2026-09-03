# Triple matching report: 696

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Maziar_Bahari | hasEmployer | Newsweek |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| To_Light_a_Candle | hasDirector | Maziar_Bahari |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Maziar_Bahari | type | Person |
| Maziar_Bahari | type | NamedIndividual |
| Maziar_Bahari | label | "Maziar Bahari" |
| Newsweek | type | Organization |
| Newsweek | type | NamedIndividual |
| Newsweek | label | "Newsweek" |
| To_Light_a_Candle | hasCreator | Maziar_Bahari |
| To_Light_a_Candle | type | Film |
| To_Light_a_Candle | type | NamedIndividual |
| To_Light_a_Candle | label | "To Light a Candle" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
