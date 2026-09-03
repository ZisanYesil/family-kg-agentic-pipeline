# Triple matching report: 854

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Eric_Mueller | hasCountry | United_States |
| World_and_Time_Enough | hasDirector | Eric_Mueller |

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
| Eric_Mueller | type | Person |
| Eric_Mueller | type | NamedIndividual |
| Eric_Mueller | label | "Eric Mueller" |
| United_States | type | Country |
| United_States | type | NamedIndividual |
| United_States | label | "United States" |
| World_and_Time_Enough | type | Film |
| World_and_Time_Enough | type | NamedIndividual |
| World_and_Time_Enough | label | "World And Time Enough" |

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
