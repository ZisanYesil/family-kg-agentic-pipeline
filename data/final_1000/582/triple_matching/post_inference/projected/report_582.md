# Triple matching report: 582

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Anđelko_Klobučar | hasAwardReceived | Vladimir_Nazor_Award |
| Anđelko_Klobučar | type | Agent |
| Anđelko_Klobučar | type | Person |
| Black_Birds | hasComposer | Anđelko_Klobučar |
| Black_Birds | hasCreator | Anđelko_Klobučar |
| Black_Birds | type | Artifact |
| Black_Birds | type | CreativeWork |
| Vladimir_Nazor_Award | type | Award |

# 2. Unmatched triples

**Total unmatched count: 5**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Anđelko_Klobučar | hasAwardReceived | porin_lifetime_award |
| Anđelko_Klobučar | hasBirthDate | "1931-07-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Anđelko_Klobučar | hasDeathDate | "2016-08-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Black_Birds | type | Film |
| porin_lifetime_award | type | Award |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 13 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 5 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.615385 |
| Recall | 1.000000 |
| F1 score | 0.761905 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
