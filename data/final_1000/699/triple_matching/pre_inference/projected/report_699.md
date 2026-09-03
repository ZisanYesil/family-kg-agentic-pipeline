# Triple matching report: 699

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Mike_Ashley | hasEmployer | Sports_Direct |
| St_James_Holdings | hasFounder | Mike_Ashley |

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
| Mike_Ashley | type | Person |
| Mike_Ashley | type | NamedIndividual |
| Mike_Ashley | label | "Mike Ashley" |
| Mike_Ashley | altLabel | "Michael James Wallace Ashley" |
| Sports_Direct | type | Organization |
| Sports_Direct | type | NamedIndividual |
| Sports_Direct | label | "Sports Direct" |
| St_James_Holdings | type | Organization |
| St_James_Holdings | type | NamedIndividual |
| St_James_Holdings | label | "St James Holdings Limited" |
| St_James_Holdings | altLabel | "St James Holdings" |

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
