# Triple matching report: 666

# 1. Matched triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Hearts_in_Exile_1915_film | hasCreator | James_Young |
| Hearts_in_Exile_1915_film | hasDirector | James_Young |
| Hearts_in_Exile_1915_film | type | Artifact |
| Hearts_in_Exile_1915_film | type | CreativeWork |
| Hearts_in_Exile_1915_film | type | Film |
| James_Young | type | Agent |
| James_Young | type | Person |
| Lawson_Harris | hasCountry | American |
| Lawson_Harris | type | Agent |
| Lawson_Harris | type | Person |
| Sunshine_Sally | hasCreator | Lawson_Harris |
| Sunshine_Sally | hasDirector | Lawson_Harris |
| Sunshine_Sally | type | Artifact |
| Sunshine_Sally | type | CreativeWork |
| Sunshine_Sally | type | Film |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| James_Young_director | hasCountry | American |
| James_Young_director | type | Agent |
| James_Young_director | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| James_Young | hasCountry | American |

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
