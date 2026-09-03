# Triple matching report: 897

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Fred_Jackman | hasDeathPlace | Hollywood |
| The_King_of_the_Wild_Horses | hasDirector | Fred_Jackman |

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
| Fred_Jackman | type | Person |
| Fred_Jackman | type | NamedIndividual |
| Fred_Jackman | label | "Fred Wood Jackman Sr." |
| Fred_Jackman | altLabel | "Fred Jackman" |
| Hollywood | type | Place |
| Hollywood | type | NamedIndividual |
| Hollywood | label | "Hollywood, California" |
| The_King_of_the_Wild_Horses | type | Film |
| The_King_of_the_Wild_Horses | type | NamedIndividual |
| The_King_of_the_Wild_Horses | label | "The King of the Wild Horses (1924 film)" |

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
