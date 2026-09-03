# Triple matching report: 878

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Berengaria_of_Barcelona | hasDeathPlace | Palencia |
| Sancha_of_Castile_Queen_of_Navarre | hasParent | Berengaria_of_Barcelona |

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
| Berengaria_of_Barcelona | type | Person |
| Berengaria_of_Barcelona | type | NamedIndividual |
| Berengaria_of_Barcelona | label | "Berengaria of Barcelona" |
| Berengaria_of_Barcelona | altLabel | "Berengaria of Barcelona" |
| Berengaria_of_Barcelona | altLabel | "Berenguela de Barcelona" |
| Palencia | type | Place |
| Palencia | type | NamedIndividual |
| Palencia | label | "Palencia" |
| Palencia | altLabel | "Palencia" |
| Sancha_of_Castile_Queen_of_Navarre | type | Person |
| Sancha_of_Castile_Queen_of_Navarre | type | NamedIndividual |
| Sancha_of_Castile_Queen_of_Navarre | label | "Sancha of Castile" |
| Sancha_of_Castile_Queen_of_Navarre | altLabel | "Sancha of Castile" |

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
