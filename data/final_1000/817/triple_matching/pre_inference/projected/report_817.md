# Triple matching report: 817

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Bruno_Mars | hasAwardReceived | Grammy_Award |
| Marry_You | hasPerformer | Bruno_Mars |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Bruno_Mars | type | Person |
| Bruno_Mars | type | NamedIndividual |
| Bruno_Mars | label | "Bruno Mars" |
| Grammy_Award | type | Award |
| Grammy_Award | type | NamedIndividual |
| Grammy_Award | label | "Grammy Award" |
| Marry_You | type | MusicalWork |
| Marry_You | type | NamedIndividual |
| Marry_You | label | "Marry You" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
