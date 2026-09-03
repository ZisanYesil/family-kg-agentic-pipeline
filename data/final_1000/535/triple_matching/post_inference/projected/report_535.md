# Triple matching report: 535

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Robert_de_Brus_4th_Lord_of_Annandale | hasParent | William_de_Brus_3rd_Lord_of_Annandale |
| Robert_de_Brus_4th_Lord_of_Annandale | type | Agent |
| Robert_de_Brus_4th_Lord_of_Annandale | type | Person |
| William_de_Brus_3rd_Lord_of_Annandale | hasChild | Robert_de_Brus_4th_Lord_of_Annandale |
| William_de_Brus_3rd_Lord_of_Annandale | type | Agent |
| William_de_Brus_3rd_Lord_of_Annandale | type | Person |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Robert_III_de_Brus | hasSibling | William_de_Brus_3rd_Lord_of_Annandale |
| Robert_III_de_Brus | type | Agent |
| Robert_III_de_Brus | type | Person |
| William_de_Brus_3rd_Lord_of_Annandale | hasSibling | Robert_III_de_Brus |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| William_de_Brus_3rd_Lord_of_Annandale | hasSibling | robert_de_brus_uncle |
| robert_de_brus_uncle | hasSibling | William_de_Brus_3rd_Lord_of_Annandale |
| robert_de_brus_uncle | type | Agent |
| robert_de_brus_uncle | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 14 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.600000 |
| Recall | 0.600000 |
| F1 score | 0.600000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
