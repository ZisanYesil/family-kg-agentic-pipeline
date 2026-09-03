# Triple matching report: 425

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Brisa_Auto_estradas_de_Portugal | hasFounder | Jorge_de_Brito |
| Brisa_Auto_estradas_de_Portugal | type | Agent |
| Brisa_Auto_estradas_de_Portugal | type | Organization |
| Jorge_de_Brito | type | Agent |
| Jorge_de_Brito | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jorge_de_Brito | hasDeathPlace | Prazeres |
| Prazeres | type | Place |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jorge_de_Brito | hasDeathPlace | place_lisbon |
| place_lisbon | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 9 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.714286 |
| Recall | 0.714286 |
| F1 score | 0.714286 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
