# Triple matching report: 733

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alekos_Sakellarios | hasBurialPlace | First_Cemetery_of_Athens |
| Maiden_s_Cheek | hasDirector | Alekos_Sakellarios |

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
| Alekos_Sakellarios | type | Person |
| Alekos_Sakellarios | type | NamedIndividual |
| Alekos_Sakellarios | label | "Alekos Sakellarios" |
| First_Cemetery_of_Athens | type | Place |
| First_Cemetery_of_Athens | type | NamedIndividual |
| First_Cemetery_of_Athens | label | "First Cemetery of Athens" |
| Maiden_s_Cheek | type | Film |
| Maiden_s_Cheek | type | NamedIndividual |
| Maiden_s_Cheek | label | "Maiden's Cheek" |

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
