# Triple matching report: 760

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Amado_V_Hernandez | hasSpouse | Atang_de_la_Rama |
| Amado_V_Hernandez | type | Agent |
| Amado_V_Hernandez | type | Person |
| Atang_de_la_Rama | hasSpouse | Amado_V_Hernandez |
| Atang_de_la_Rama | type | Agent |
| Atang_de_la_Rama | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Amado_V_Hernandez | hasBirthPlace | Hagonoy |
| Hagonoy | type | Place |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Amado_V_Hernandez | hasBirthPlace | tondo_manila |
| tondo_manila | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 10 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.750000 |
| Recall | 0.750000 |
| F1 score | 0.750000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
