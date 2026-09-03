# Triple matching report: 909

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jim_Wynorski | hasBirthPlace | New_York |
| Not_of_This_Earth | hasDirector | Jim_Wynorski |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Jim_Wynorski | type | Person |
| Jim_Wynorski | type | NamedIndividual |
| Jim_Wynorski | label | "Jim Wynorski" |
| New_York | type | Place |
| New_York | type | NamedIndividual |
| New_York | label | "Glen Cove, Long Island, New York" |
| Not_of_This_Earth | type | Film |
| Not_of_This_Earth | type | NamedIndividual |
| Not_of_This_Earth | label | "Not of This Earth (1988 film)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
