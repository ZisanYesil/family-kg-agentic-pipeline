# Triple matching report: 275

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Brand_New_Immortals | type | Agent |
| Brand_New_Immortals | type | Organization |
| David_Ryan_Harris | hasBirthPlace | Evanston_Illinois |
| David_Ryan_Harris | type | Agent |
| David_Ryan_Harris | type | Person |
| Evanston_Illinois | type | Place |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Brand_New_Immortals | hasMember | David_Ryan_Harris |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Brand_New_Immortals | hasFounder | David_Ryan_Harris |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 7 |
| Ground-truth triples in scope | 7 |
| Union triples in scope | 8 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.857143 |
| Recall | 0.857143 |
| F1 score | 0.857143 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
