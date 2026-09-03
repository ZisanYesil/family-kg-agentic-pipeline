# Triple matching report: 330

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Drogo_of_Champagne | hasParent | Plectrudis |
| Plectrude | hasSpouse | Pepin_of_Herstal |

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Drogo_of_Champagne | type | Person |
| Drogo_of_Champagne | type | NamedIndividual |
| Drogo_of_Champagne | label | "Drogo of Champagne" |
| Pepin_of_Herstal | hasParent | Drogo_of_Champagne |
| Pepin_of_Herstal | type | Person |
| Pepin_of_Herstal | type | NamedIndividual |
| Pepin_of_Herstal | label | "Pippin of Heristal" |
| Pepin_of_Herstal | altLabel | "Pepin of Heristal" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
