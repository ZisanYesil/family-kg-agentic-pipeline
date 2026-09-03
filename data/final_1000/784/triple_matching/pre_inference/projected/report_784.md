# Triple matching report: 784

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Bruno_Mars | hasAwardReceived | Grammy_Award |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Talking_to_the_Moon | hasComposer | Bruno_Mars |

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
| Talking_to_the_Moon | type | CreativeWork |
| Talking_to_the_Moon | type | NamedIndividual |
| Talking_to_the_Moon | label | "Talking to the Moon" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.100000 |
| Recall | 0.500000 |
| F1 score | 0.166667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
