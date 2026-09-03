# Triple matching report: 110

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| 3096_Days | hasCreator | Sherry_Horman |
| 3096_Days | hasDirector | Sherry_Horman |
| 3096_Days | type | Artifact |
| 3096_Days | type | CreativeWork |
| 3096_Days | type | Film |
| American | type | Country |
| American | type | Place |
| Sherry_Horman | hasCountry | American |
| Sherry_Horman | type | Agent |
| Sherry_Horman | type | Person |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Sherry_Horman | hasCountry | country_germany |
| country_germany | type | Country |
| country_germany | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 13 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.769231 |
| Recall | 1.000000 |
| F1 score | 0.869565 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
