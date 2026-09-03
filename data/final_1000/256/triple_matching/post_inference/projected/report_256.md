# Triple matching report: 256

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Filmfare_Award | type | Award |
| Howrah_Bridge | type | Artifact |
| Howrah_Bridge | type | CreativeWork |
| O_P_Nayyar | hasAwardReceived | Filmfare_Award |
| O_P_Nayyar | type | Agent |
| O_P_Nayyar | type | Person |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Howrah_Bridge | hasComposer | O_P_Nayyar |
| Howrah_Bridge | hasCreator | O_P_Nayyar |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Howrah_Bridge | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 9 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.857143 |
| Recall | 0.750000 |
| F1 score | 0.800000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
