# Triple matching report: 425

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Brisa_Auto_estradas_de_Portugal | hasFounder | Jorge_de_Brito |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Jorge_de_Brito | hasDeathPlace | Prazeres |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Brisa_Auto_estradas_de_Portugal | type | Organization |
| Brisa_Auto_estradas_de_Portugal | type | NamedIndividual |
| Brisa_Auto_estradas_de_Portugal | label | "Brisa – Auto-estradas de Portugal" |
| Jorge_de_Brito | hasDeathPlace | place_lisbon |
| Jorge_de_Brito | type | Person |
| Jorge_de_Brito | type | NamedIndividual |
| Jorge_de_Brito | label | "Jorge Artur Rego de Brito" |
| Jorge_de_Brito | altLabel | "Jorge de Brito" |
| place_lisbon | type | Place |
| place_lisbon | type | NamedIndividual |
| place_lisbon | label | "Lisbon" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
