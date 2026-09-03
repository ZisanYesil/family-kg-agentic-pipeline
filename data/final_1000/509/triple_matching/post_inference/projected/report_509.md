# Triple matching report: 509

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Charles_Orlando_Dauphin_of_France | hasParent | Charles_VIII_of_France |
| Charles_Orlando_Dauphin_of_France | type | Agent |
| Charles_Orlando_Dauphin_of_France | type | Person |
| Charles_VIII_of_France | hasChild | Charles_Orlando_Dauphin_of_France |
| Charles_VIII_of_France | type | Agent |
| Charles_VIII_of_France | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Charles_VIII_of_France | hasCauseOfDeath | stroke |
| stroke | type | CauseOfDeath |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Charles_VIII_of_France | hasCauseOfDeath | accidental_head_injury |
| accidental_head_injury | type | CauseOfDeath |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 10 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.750000 |
| Recall | 0.750000 |
| F1 score | 0.750000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
