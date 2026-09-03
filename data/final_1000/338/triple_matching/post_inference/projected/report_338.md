# Triple matching report: 338

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Francis_William_Thring | type | Agent |
| Francis_William_Thring | type | Person |
| His_Royal_Highness | type | Artifact |
| His_Royal_Highness | type | CreativeWork |
| His_Royal_Highness | type | Film |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| F_W_Thring | hasChild | Francis_William_Thring |
| F_W_Thring | type | Agent |
| F_W_Thring | type | Person |
| Francis_William_Thring | hasParent | F_W_Thring |
| His_Royal_Highness | hasCreator | F_W_Thring |
| His_Royal_Highness | hasDirector | F_W_Thring |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| His_Royal_Highness | hasCreator | Francis_William_Thring |
| His_Royal_Highness | hasDirector | Francis_William_Thring |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 13 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.714286 |
| Recall | 0.454545 |
| F1 score | 0.555556 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
