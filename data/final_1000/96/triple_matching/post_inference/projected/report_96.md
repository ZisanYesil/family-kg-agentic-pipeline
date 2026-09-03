# Triple matching report: 96

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Anne_Castles | hasOccupation | cognitive_scientist |
| Anne_Castles | type | Agent |
| Anne_Castles | type | Person |
| Colin_Will | hasOccupation | poet |
| Colin_Will | hasOccupation | publisher |
| Colin_Will | type | Agent |
| Colin_Will | type | Person |
| cognitive_scientist | type | Occupation |
| poet | type | Occupation |
| publisher | type | Occupation |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Colin_Will | hasOccupation | librarian |
| librarian | type | Occupation |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 12 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 2 |
| Precision | 1.000000 |
| Recall | 0.833333 |
| F1 score | 0.909091 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
