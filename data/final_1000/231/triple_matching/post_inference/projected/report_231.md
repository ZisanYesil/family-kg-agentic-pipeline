# Triple matching report: 231

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Diamond_Head | hasComposer | John_Williams |
| Diamond_Head | hasCreator | John_Williams |
| Diamond_Head | type | Artifact |
| Diamond_Head | type | CreativeWork |
| John_Williams | hasCountry | American |
| John_Williams | type | Agent |
| John_Williams | type | Person |

# 2. Unmatched triples

**Total unmatched count: 1**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Diamond_Head | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 10 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.900000 |
| Recall | 1.000000 |
| F1 score | 0.947368 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
