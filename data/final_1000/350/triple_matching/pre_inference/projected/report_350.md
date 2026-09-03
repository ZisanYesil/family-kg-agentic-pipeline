# Triple matching report: 350

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Dietrich_Mateschitz | hasCountry | Austrian |
| Red_Bull_Racing_Team | hasFounder | Dietrich_Mateschitz |

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
| Austrian | type | Country |
| Austrian | type | NamedIndividual |
| Austrian | label | "Austria" |
| Austrian | altLabel | "Austrian" |
| Dietrich_Mateschitz | type | Person |
| Dietrich_Mateschitz | type | NamedIndividual |
| Dietrich_Mateschitz | label | "Dietrich Mateschitz" |
| Red_Bull_Racing_Team | type | Organization |
| Red_Bull_Racing_Team | type | NamedIndividual |
| Red_Bull_Racing_Team | label | "Team Red Bull (NASCAR team)" |

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
