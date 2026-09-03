# Triple matching report: 587

# 1. Matched triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Aditya_Bhattacharya | hasParent | Basu_Bhattacharya |
| Aditya_Bhattacharya | type | Agent |
| Aditya_Bhattacharya | type | Person |
| Basu_Bhattacharya | hasChild | Aditya_Bhattacharya |
| Basu_Bhattacharya | type | Agent |
| Basu_Bhattacharya | type | Person |
| Griha_Pravesh | hasCreator | Basu_Bhattacharya |
| Griha_Pravesh | hasDirector | Basu_Bhattacharya |
| Griha_Pravesh | type | Artifact |
| Griha_Pravesh | type | CreativeWork |
| Griha_Pravesh | type | Film |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Basu_Bhattacharya | hasChild | anwesha_arya |
| Basu_Bhattacharya | hasChild | chimmu |
| anwesha_arya | hasParent | Basu_Bhattacharya |
| anwesha_arya | type | Agent |
| anwesha_arya | type | Person |
| chimmu | hasParent | Basu_Bhattacharya |
| chimmu | type | Agent |
| chimmu | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 19 |
| True positives (matched) | 11 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.578947 |
| Recall | 1.000000 |
| F1 score | 0.733333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
