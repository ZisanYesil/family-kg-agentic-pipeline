# Triple matching report: 578

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Marcel_Varnel | hasDeathPlace | West_Sussex |
| The_Loves_of_Madame_Dubarry | hasDirector | Marcel_Varnel |

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
| Marcel_Varnel | type | Person |
| Marcel_Varnel | type | NamedIndividual |
| Marcel_Varnel | label | "Marcel Varnel" |
| The_Loves_of_Madame_Dubarry | type | Film |
| The_Loves_of_Madame_Dubarry | type | NamedIndividual |
| The_Loves_of_Madame_Dubarry | label | "The Loves of Madame Dubarry" |
| The_Loves_of_Madame_Dubarry | altLabel | "I Give My Heart" |
| West_Sussex | type | Place |
| West_Sussex | type | NamedIndividual |
| West_Sussex | label | "Rake, West Sussex" |

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
