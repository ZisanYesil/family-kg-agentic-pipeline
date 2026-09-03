# Triple matching report: 346

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Hubert_Mordek | hasBirthDate | "1939-05-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Hubert_Mordek | hasDeathDate | "2006-03-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Levon_Ashotovich_Grigorian | hasBirthDate | "1947-09-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Levon_Ashotovich_Grigorian | hasDeathDate | "1975-11-29"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Hubert_Mordek | type | Person |
| Hubert_Mordek | type | NamedIndividual |
| Hubert_Mordek | label | "Hubert Mordek" |
| Levon_Ashotovich_Grigorian | type | Person |
| Levon_Ashotovich_Grigorian | type | NamedIndividual |
| Levon_Ashotovich_Grigorian | label | "Levon Ashotovich Grigorian" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 10 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.400000 |
| Recall | 1.000000 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
