# Triple matching report: 752

# 1. Matched triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Gallopin_Gals | hasCreator | Joseph_Barbera |
| Gallopin_Gals | hasDirector | Joseph_Barbera |
| Gallopin_Gals | type | Artifact |
| Gallopin_Gals | type | CreativeWork |
| Gallopin_Gals | type | Film |
| Joseph_Barbera | type | Agent |
| Joseph_Barbera | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Joseph_Barbera | hasEmployer | Van_Beuren_Studios |
| Van_Beuren_Studios | type | Agent |
| Van_Beuren_Studios | type | Organization |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Joseph_Barbera | hasEmployer | organization_metro_golden_mayer |
| organization_metro_golden_mayer | type | Agent |
| organization_metro_golden_mayer | type | Organization |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 13 |
| True positives (matched) | 7 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.700000 |
| Recall | 0.700000 |
| F1 score | 0.700000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
