# Triple matching report: 760

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Atang_de_la_Rama | hasSpouse | Amado_V_Hernandez |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Amado_V_Hernandez | hasBirthPlace | Hagonoy |

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Amado_V_Hernandez | hasBirthPlace | tondo_manila |
| Amado_V_Hernandez | type | Person |
| Amado_V_Hernandez | type | NamedIndividual |
| Amado_V_Hernandez | label | "Amado V. Hernandez" |
| Amado_V_Hernandez | altLabel | "Amado V. Hernandez" |
| Amado_V_Hernandez | altLabel | "Amado Vera Hernandez" |
| Atang_de_la_Rama | type | Person |
| Atang_de_la_Rama | type | NamedIndividual |
| Atang_de_la_Rama | label | "Atang de la Rama" |
| Atang_de_la_Rama | altLabel | "Atang de la Rama" |
| Atang_de_la_Rama | altLabel | "Honorata de la Rama-Hernandez" |
| tondo_manila | type | Place |
| tondo_manila | type | NamedIndividual |
| tondo_manila | label | "Tondo, Manila" |
| tondo_manila | altLabel | "Tondo, Manila" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
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
