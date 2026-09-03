# Triple matching report: 299

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| The_Gold_Cure | hasDirector | W_P_Kellino |
| W_P_Kellino | hasBirthPlace | London |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| London | type | Place |
| London | type | NamedIndividual |
| London | label | "London, England" |
| The_Gold_Cure | type | Film |
| The_Gold_Cure | type | NamedIndividual |
| The_Gold_Cure | label | "The Gold Cure (1925 film)" |
| W_P_Kellino | type | Person |
| W_P_Kellino | type | NamedIndividual |
| W_P_Kellino | label | "W.P. Kellino" |
| W_P_Kellino | altLabel | "W.P. Kellino" |
| W_P_Kellino | altLabel | "William Philip Gislingham" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
