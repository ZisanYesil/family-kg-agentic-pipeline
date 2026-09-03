# Triple matching report: 582

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Anđelko_Klobučar | hasAwardReceived | Vladimir_Nazor_Award |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Black_Birds | hasComposer | Anđelko_Klobučar |

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Anđelko_Klobučar | hasAwardReceived | porin_lifetime_award |
| Anđelko_Klobučar | hasBirthDate | "1931-07-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Anđelko_Klobučar | hasDeathDate | "2016-08-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Anđelko_Klobučar | type | Person |
| Anđelko_Klobučar | type | NamedIndividual |
| Anđelko_Klobučar | label | "Anđelko Klobučar" |
| Black_Birds | type | Film |
| Black_Birds | type | NamedIndividual |
| Black_Birds | label | "Black Birds" |
| Vladimir_Nazor_Award | type | Award |
| Vladimir_Nazor_Award | type | NamedIndividual |
| Vladimir_Nazor_Award | label | "Vladimir Nazor Award for Life Achievement in Music" |
| porin_lifetime_award | type | Award |
| porin_lifetime_award | type | NamedIndividual |
| porin_lifetime_award | label | "Porin Lifetime Achievement Award" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 17 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.062500 |
| Recall | 0.500000 |
| F1 score | 0.111111 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
