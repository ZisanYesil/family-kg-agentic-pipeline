# Triple matching report: 982

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Strange_Boarders | hasDirector | Herbert_Mason |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Herbert_Mason | hasBirthPlace | Birmingham |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Herbert_Mason | type | Person |
| Herbert_Mason | type | NamedIndividual |
| Herbert_Mason | label | "Herbert Mason" |
| Herbert_Mason | altLabel | "Samuel George Herbert Mason" |
| Strange_Boarders | type | Film |
| Strange_Boarders | type | NamedIndividual |
| Strange_Boarders | label | "Strange Boarders" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.125000 |
| Recall | 0.500000 |
| F1 score | 0.200000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
