# Triple matching report: 876

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Mariam_El_Masri | hasBirthDate | "1991-06-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Marie_Agba_Otikpo | hasBirthDate | "1948-12-01"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Mariam_El_Masri | type | Person |
| Mariam_El_Masri | type | NamedIndividual |
| Mariam_El_Masri | label | "Mariam El-Masri" |
| Mariam_El_Masri | altLabel | "Mariam El Masri" |
| Marie_Agba_Otikpo | type | Person |
| Marie_Agba_Otikpo | type | NamedIndividual |
| Marie_Agba_Otikpo | label | "Marie Agba-Otikpo" |
| Marie_Agba_Otikpo | altLabel | "Marie Belkine" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
