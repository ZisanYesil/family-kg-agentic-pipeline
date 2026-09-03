# Triple matching report: 778

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Eri_Jabotinsky | hasParent | Ze_ev_Jabotinsky |
| Ze_ev_Jabotinsky | hasDeathPlace | Hunter |

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
| Eri_Jabotinsky | type | Person |
| Eri_Jabotinsky | type | NamedIndividual |
| Eri_Jabotinsky | label | "Eri Jabotinsky" |
| Hunter | type | Place |
| Hunter | type | NamedIndividual |
| Hunter | label | "Hunter, New York" |
| Ze_ev_Jabotinsky | type | Person |
| Ze_ev_Jabotinsky | type | NamedIndividual |
| Ze_ev_Jabotinsky | label | "Ze'ev Jabotinsky" |

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
