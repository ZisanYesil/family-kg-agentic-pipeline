# Triple matching report: 528

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Sir_Edward_Acton_3rd_Baronet | hasParent | Sir_Walter_Acton_2nd_Baronet |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Sir_Walter_Acton | hasCountry | English |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| English | type | Country |
| English | type | NamedIndividual |
| English | label | "United Kingdom" |
| English | altLabel | "English" |
| Sir_Edward_Acton_3rd_Baronet | type | Person |
| Sir_Edward_Acton_3rd_Baronet | type | NamedIndividual |
| Sir_Edward_Acton_3rd_Baronet | label | "Sir Edward Acton, 3rd Baronet" |
| Sir_Walter_Acton_2nd_Baronet | hasCountry | English |
| Sir_Walter_Acton_2nd_Baronet | type | Person |
| Sir_Walter_Acton_2nd_Baronet | type | NamedIndividual |
| Sir_Walter_Acton_2nd_Baronet | label | "Sir Walter Acton, 2nd Baronet" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
