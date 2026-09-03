# Triple matching report: 917

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Deathstalker_II | hasDirector | Jim_Wynorski |
| Jim_Wynorski | hasBirthPlace | New_York |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Deathstalker_II | type | Film |
| Deathstalker_II | type | NamedIndividual |
| Deathstalker_II | label | "Deathstalker II" |
| Jim_Wynorski | type | Person |
| Jim_Wynorski | type | NamedIndividual |
| Jim_Wynorski | label | "Jim Wynorski" |
| New_York | type | Place |
| New_York | type | NamedIndividual |
| New_York | label | "Glen Cove, Long Island, New York" |
| New_York | altLabel | "Glen Cove" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
