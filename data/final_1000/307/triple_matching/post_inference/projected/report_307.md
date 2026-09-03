# Triple matching report: 307

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Finland | type | Country |
| Finland | type | Place |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Tommys | hasCountry | Finland |
| Tommys | type | Artifact |
| Vocal_Spectrum | hasCountry | American |
| Vocal_Spectrum | type | Artifact |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| tommys_organization | hasCountry | Finland |
| tommys_organization | type | Agent |
| tommys_organization | type | Organization |
| vocal_spectrum_organization | hasCountry | American |
| vocal_spectrum_organization | type | Agent |
| vocal_spectrum_organization | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 14 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.400000 |
| Recall | 0.500000 |
| F1 score | 0.444444 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
