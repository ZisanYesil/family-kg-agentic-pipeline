# Triple matching report: 549

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Latin_Moon | type | Artifact |
| Latin_Moon | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Latin_Moon | hasCreator | Massari |
| Latin_Moon | hasPerformer | Massari |
| Lebanese | type | Country |
| Lebanese | type | Place |
| Massari | hasCountry | Lebanese |
| Massari | type | Agent |
| Massari | type | Person |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Latin_Moon | hasCreator | mia_martina |
| Latin_Moon | hasPerformer | mia_martina |
| canada | type | Country |
| canada | type | Place |
| mia_martina | hasCountry | canada |
| mia_martina | type | Agent |
| mia_martina | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 1 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 16 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 7 |
| Precision | 0.222222 |
| Recall | 0.222222 |
| F1 score | 0.222222 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
