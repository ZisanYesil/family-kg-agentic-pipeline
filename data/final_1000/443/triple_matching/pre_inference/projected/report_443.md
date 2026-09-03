# Triple matching report: 443

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Chandrakant_Kulkarni | hasCountry | India |
| Family_Katta | hasDirector | Chandrakant_Kulkarni |
| P_Venu | hasCountry | India |
| Ward_No_7 | hasDirector | P_Venu |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Chandrakant_Kulkarni | type | Person |
| Chandrakant_Kulkarni | type | NamedIndividual |
| Chandrakant_Kulkarni | label | "Chandrakant Kulkarni" |
| Family_Katta | type | Film |
| Family_Katta | type | NamedIndividual |
| Family_Katta | label | "Family Katta" |
| India | type | Country |
| India | type | NamedIndividual |
| India | label | "India" |
| India | altLabel | "Indian" |
| P_Venu | type | Person |
| P_Venu | type | NamedIndividual |
| P_Venu | label | "P. Venu" |
| Ward_No_7 | type | Film |
| Ward_No_7 | type | NamedIndividual |
| Ward_No_7 | label | "Ward No.7" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 20 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
