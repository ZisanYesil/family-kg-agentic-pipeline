# Triple matching report: 44

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Bernhard_Afinger | hasBirthDate | "1813-05-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Bernhard_Afinger | hasDeathDate | "1882-12-25"^^<http://www.w3.org/2001/XMLSchema#date> |
| Melvin_Kranzberg | hasBirthDate | "1917-11-22"^^<http://www.w3.org/2001/XMLSchema#date> |
| Melvin_Kranzberg | hasDeathDate | "1995-12-06"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Bernhard_Afinger | type | Person |
| Bernhard_Afinger | type | NamedIndividual |
| Bernhard_Afinger | label | "Bernhard Afinger" |
| Melvin_Kranzberg | type | Person |
| Melvin_Kranzberg | type | NamedIndividual |
| Melvin_Kranzberg | label | "Melvin Kranzberg" |

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
