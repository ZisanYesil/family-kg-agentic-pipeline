# Triple matching report: 547

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Bottle_Caps | hasManufacturer | Nestlé |
| Nestlé | hasCountry | Swiss |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Bottle_Caps | type | Product |
| Bottle_Caps | type | NamedIndividual |
| Bottle_Caps | label | "Bottle Caps" |
| Bottle_Caps | altLabel | "Bottle Caps (candy)" |
| Nestlé | type | Organization |
| Nestlé | type | NamedIndividual |
| Nestlé | label | "Nestlé" |
| Nestlé | altLabel | "Nestlé" |
| Nestlé | altLabel | "Nestlé S.A." |
| Swiss | type | Country |
| Swiss | type | NamedIndividual |
| Swiss | label | "Switzerland" |
| Swiss | altLabel | "Swiss" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
