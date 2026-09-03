# Triple matching report: 555

# 1. Matched triples

**Count: 19**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Blake_Edwards | hasCountry | American |
| Blake_Edwards | type | Agent |
| Blake_Edwards | type | Person |
| British | type | Country |
| British | type | Place |
| Operation_Petticoat | hasCreator | Blake_Edwards |
| Operation_Petticoat | hasDirector | Blake_Edwards |
| Operation_Petticoat | type | Artifact |
| Operation_Petticoat | type | CreativeWork |
| Operation_Petticoat | type | Film |
| Tom_Harper | type | Agent |
| Tom_Harper | type | Person |
| War_Book | hasCreator | Tom_Harper |
| War_Book | hasDirector | Tom_Harper |
| War_Book | type | Artifact |
| War_Book | type | CreativeWork |
| War_Book | type | Film |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Tom_Harper_director | hasCountry | British |
| Tom_Harper_director | type | Agent |
| Tom_Harper_director | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Tom_Harper | hasCountry | British |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 6 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 22 |
| Union triples in scope | 23 |
| True positives (matched) | 19 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.950000 |
| Recall | 0.863636 |
| F1 score | 0.904762 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
