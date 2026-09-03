# Triple matching report: 452

# 1. Matched triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Frank_Arnold | hasCountry | American |
| Frank_Arnold | type | Agent |
| Frank_Arnold | type | Person |
| John_Cromwell | type | Agent |
| John_Cromwell | type | Person |
| Ripkin | hasCreator | Frank_Arnold |
| Ripkin | hasDirector | Frank_Arnold |
| Ripkin | type | Artifact |
| Ripkin | type | CreativeWork |
| Ripkin | type | Film |
| This_Man_Is_Mine_1934_film | hasCreator | John_Cromwell |
| This_Man_Is_Mine_1934_film | hasDirector | John_Cromwell |
| This_Man_Is_Mine_1934_film | type | Artifact |
| This_Man_Is_Mine_1934_film | type | CreativeWork |
| This_Man_Is_Mine_1934_film | type | Film |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| John_Cromwell_director | hasCountry | American |
| John_Cromwell_director | type | Agent |
| John_Cromwell_director | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| John_Cromwell | hasCountry | American |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 20 |
| Union triples in scope | 21 |
| True positives (matched) | 17 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.944444 |
| Recall | 0.850000 |
| F1 score | 0.894737 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
