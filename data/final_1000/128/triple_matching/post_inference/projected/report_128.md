# Triple matching report: 128

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| English | type | Country |
| English | type | Place |
| Leicester_Devereux_6th_Viscount_Hereford | hasParent | Walter_Devereux_5th_Viscount_Hereford |
| Leicester_Devereux_6th_Viscount_Hereford | type | Agent |
| Leicester_Devereux_6th_Viscount_Hereford | type | Person |
| Walter_Devereux_5th_Viscount_Hereford | hasChild | Leicester_Devereux_6th_Viscount_Hereford |
| Walter_Devereux_5th_Viscount_Hereford | type | Agent |
| Walter_Devereux_5th_Viscount_Hereford | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Walter_Devereux | hasCountry | English |
| Walter_Devereux | type | Agent |
| Walter_Devereux | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Walter_Devereux_5th_Viscount_Hereford | hasCountry | English |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 12 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.888889 |
| Recall | 0.727273 |
| F1 score | 0.800000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
