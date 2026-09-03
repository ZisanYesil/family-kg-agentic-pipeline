# Triple matching report: 413

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Call_for_Help | type | Artifact |
| Call_for_Help | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Call_for_Help | hasCreator | Leo_Laporte |
| Leo_Laporte | hasEmployer | TWiT_tv |
| Leo_Laporte | type | Agent |
| Leo_Laporte | type | Person |
| TWiT_tv | type | Agent |
| TWiT_tv | type | Organization |

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Call_for_Help | hasPresenter | person_chris_pirillo |
| org_lockergnome_inc | hasFounder | person_chris_pirillo |
| org_lockergnome_inc | type | Agent |
| org_lockergnome_inc | type | Organization |
| person_chris_pirillo | type | Agent |
| person_chris_pirillo | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 1 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 6 |
| Precision | 0.250000 |
| Recall | 0.250000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
