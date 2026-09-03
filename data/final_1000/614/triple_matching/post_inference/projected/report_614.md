# Triple matching report: 614

# 1. Matched triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Bhanumathi_Ramakrishna | hasSpouse | P_S_Ramakrishna_Rao |
| Bhanumathi_Ramakrishna | type | Agent |
| Bhanumathi_Ramakrishna | type | Person |
| Bratuku_Teruvu | hasCreator | P_S_Ramakrishna_Rao |
| Bratuku_Teruvu | hasDirector | P_S_Ramakrishna_Rao |
| Bratuku_Teruvu | type | Artifact |
| Bratuku_Teruvu | type | CreativeWork |
| Bratuku_Teruvu | type | Film |
| P_S_Ramakrishna_Rao | hasSpouse | Bhanumathi_Ramakrishna |
| P_S_Ramakrishna_Rao | type | Agent |
| P_S_Ramakrishna_Rao | type | Person |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| P_S_Ramakrishna_Rao | hasBirthDate | "1918-10-12"^^<http://www.w3.org/2001/XMLSchema#date> |
| P_S_Ramakrishna_Rao | hasDeathDate | "1986-09-07"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 13 |
| True positives (matched) | 11 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.846154 |
| Recall | 1.000000 |
| F1 score | 0.916667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
