# Triple matching report: 614

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Bratuku_Teruvu | hasDirector | P_S_Ramakrishna_Rao |
| P_S_Ramakrishna_Rao | hasSpouse | Bhanumathi_Ramakrishna |

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
| Bhanumathi_Ramakrishna | type | Person |
| Bhanumathi_Ramakrishna | type | NamedIndividual |
| Bhanumathi_Ramakrishna | label | "Bhanumathi Ramakrishna" |
| Bratuku_Teruvu | type | Film |
| Bratuku_Teruvu | type | NamedIndividual |
| Bratuku_Teruvu | label | "Bratuku Teruvu" |
| P_S_Ramakrishna_Rao | hasBirthDate | "1918-10-12"^^<http://www.w3.org/2001/XMLSchema#date> |
| P_S_Ramakrishna_Rao | hasDeathDate | "1986-09-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| P_S_Ramakrishna_Rao | type | Person |
| P_S_Ramakrishna_Rao | type | NamedIndividual |
| P_S_Ramakrishna_Rao | label | "P. S. Ramakrishna Rao" |

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
