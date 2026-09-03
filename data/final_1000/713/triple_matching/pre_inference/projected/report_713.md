# Triple matching report: 713

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Adolf_of_Germany | hasDeathPlace | Göllheim |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Imagina_of_Isenburg_Limburg | hasSpouse | Adolf_of_Nassau |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Adolf_of_Germany | type | Person |
| Adolf_of_Germany | type | NamedIndividual |
| Adolf_of_Germany | label | "Adolf of Germany" |
| Göllheim | type | Place |
| Göllheim | type | NamedIndividual |
| Göllheim | label | "Göllheim" |
| Imagina_of_Isenburg_Limburg | hasSpouse | Adolf_of_Germany |
| Imagina_of_Isenburg_Limburg | type | Person |
| Imagina_of_Isenburg_Limburg | type | NamedIndividual |
| Imagina_of_Isenburg_Limburg | label | "Imagina of Isenburg-Limburg" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
