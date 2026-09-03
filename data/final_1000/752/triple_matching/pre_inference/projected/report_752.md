# Triple matching report: 752

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Gallopin_Gals | hasDirector | Joseph_Barbera |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Joseph_Barbera | hasEmployer | Van_Beuren_Studios |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Gallopin_Gals | type | Film |
| Gallopin_Gals | type | NamedIndividual |
| Gallopin_Gals | label | "Gallopin' Gals" |
| Joseph_Barbera | hasEmployer | organization_metro_golden_mayer |
| Joseph_Barbera | type | Person |
| Joseph_Barbera | type | NamedIndividual |
| Joseph_Barbera | label | "Joseph Barbera" |
| Joseph_Barbera | altLabel | "Joseph Roland Barbera" |
| organization_metro_golden_mayer | type | Organization |
| organization_metro_golden_mayer | type | NamedIndividual |
| organization_metro_golden_mayer | label | "Metro‑Goldwyn‑Mayer" |
| organization_metro_golden_mayer | altLabel | "MGM" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
