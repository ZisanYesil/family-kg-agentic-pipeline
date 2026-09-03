# Triple matching report: 703

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Frank_Hall_Crane | hasCountry | America |
| Joe_Simon | hasCountry | America |
| Simha_Jodi | hasDirector | Joe_Simon |
| The_Pauper_Millionaire | hasDirector | Frank_Hall_Crane |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| America | type | Country |
| America | type | NamedIndividual |
| America | label | "United States" |
| America | altLabel | "American" |
| Frank_Hall_Crane | type | Person |
| Frank_Hall_Crane | type | NamedIndividual |
| Frank_Hall_Crane | label | "Frank Hall Crane" |
| Joe_Simon | type | Person |
| Joe_Simon | type | NamedIndividual |
| Joe_Simon | label | "Joe Simon" |
| Joe_Simon | altLabel | "Joseph Henry Simon" |
| Simha_Jodi | type | Film |
| Simha_Jodi | type | NamedIndividual |
| Simha_Jodi | label | "Simha Jodi" |
| The_Pauper_Millionaire | type | Film |
| The_Pauper_Millionaire | type | NamedIndividual |
| The_Pauper_Millionaire | label | "The Pauper Millionaire" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 21 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 21 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.190476 |
| Recall | 1.000000 |
| F1 score | 0.320000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
