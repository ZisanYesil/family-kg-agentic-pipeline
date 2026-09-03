# Triple matching report: 713

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Adolf_of_Germany | hasDeathPlace | Göllheim |
| Adolf_of_Germany | type | Agent |
| Adolf_of_Germany | type | Person |
| Göllheim | type | Place |
| Imagina_of_Isenburg_Limburg | type | Agent |
| Imagina_of_Isenburg_Limburg | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Adolf_of_Nassau | hasSpouse | Imagina_of_Isenburg_Limburg |
| Adolf_of_Nassau | type | Agent |
| Adolf_of_Nassau | type | Person |
| Imagina_of_Isenburg_Limburg | hasSpouse | Adolf_of_Nassau |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Adolf_of_Germany | hasSpouse | Imagina_of_Isenburg_Limburg |
| Imagina_of_Isenburg_Limburg | hasSpouse | Adolf_of_Germany |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 12 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.750000 |
| Recall | 0.600000 |
| F1 score | 0.666667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
