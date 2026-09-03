# Triple matching report: 134

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Gus_Meins | hasCountry | American |
| Gus_Meins | type | Agent |
| Gus_Meins | type | Person |
| Little_Papa | hasCreator | Gus_Meins |
| Little_Papa | hasDirector | Gus_Meins |
| Little_Papa | type | Artifact |
| Little_Papa | type | CreativeWork |
| Little_Papa | type | Film |

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
| Gus_Meins | hasCountry | germany |
| germany | type | Country |
| germany | type | Place |

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
