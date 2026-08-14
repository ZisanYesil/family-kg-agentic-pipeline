# Triple matching report: 6

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Q5175909 | type | Agent |
| Q5175909 | type | Person |
| Q7285226 | type | Agent |
| Q7285226 | type | Person |
| Q7320430 | type | Agent |
| Q7320430 | type | Person |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Q5175909 | hasChild | Q7320430 |
| Q5175909 | hasFather | Q7285226 |
| Q5175909 | hasParent | Q7285226 |
| Q7285226 | hasChild | Q5175909 |
| Q7320430 | hasFather | Q5175909 |
| Q7320430 | hasParent | Q5175909 |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Q5175909 | hasChild | Q7285226 |
| Q5175909 | hasFather | Q7320430 |
| Q5175909 | hasParent | Q7320430 |
| Q7285226 | hasFather | Q5175909 |
| Q7285226 | hasParent | Q5175909 |
| Q7320430 | hasChild | Q5175909 |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 18 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.500000 |
| Recall | 0.500000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
