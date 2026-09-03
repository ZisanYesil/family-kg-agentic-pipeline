# Triple matching report: 452

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Frank_Arnold | hasCountry | American |
| Ripkin | hasDirector | Frank_Arnold |
| This_Man_Is_Mine_1934_film | hasDirector | John_Cromwell |

# 2. Unmatched triples

**Total unmatched count: 18**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| John_Cromwell_director | hasCountry | American |

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Frank_Arnold | type | Person |
| Frank_Arnold | type | NamedIndividual |
| Frank_Arnold | label | "Frank Arnold" |
| John_Cromwell | hasCountry | American |
| John_Cromwell | type | Person |
| John_Cromwell | type | NamedIndividual |
| John_Cromwell | label | "John Cromwell" |
| Ripkin | type | Film |
| Ripkin | type | NamedIndividual |
| Ripkin | label | "Ripkin" |
| This_Man_Is_Mine_1934_film | type | Film |
| This_Man_Is_Mine_1934_film | type | NamedIndividual |
| This_Man_Is_Mine_1934_film | label | "This Man Is Mine (1934 film)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 21 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.150000 |
| Recall | 0.750000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
