# Triple matching report: 841

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| B_Boy | hasPerformer | Meek_Mill |
| Meek_Mill | hasDetentionPlace | State_Correctional_Institution_Chester |

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
| B_Boy | type | MusicalWork |
| B_Boy | type | NamedIndividual |
| B_Boy | label | "B Boy" |
| Meek_Mill | type | Person |
| Meek_Mill | type | NamedIndividual |
| Meek_Mill | label | "Meek Mill" |
| State_Correctional_Institution_Chester | type | Place |
| State_Correctional_Institution_Chester | type | NamedIndividual |
| State_Correctional_Institution_Chester | label | "State Correctional Institution – Chester" |

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
