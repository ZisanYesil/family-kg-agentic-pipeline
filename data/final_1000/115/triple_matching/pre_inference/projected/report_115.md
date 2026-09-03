# Triple matching report: 115

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| George_W_Bush | hasCountry | American |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Arbusto_Energy | hasFounder | President_George_W_Bush |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Arbusto_Energy | hasFounder | George_W_Bush |
| Arbusto_Energy | type | Organization |
| Arbusto_Energy | type | NamedIndividual |
| Arbusto_Energy | label | "Arbusto Energy" |
| George_W_Bush | type | Person |
| George_W_Bush | type | NamedIndividual |
| George_W_Bush | label | "George W. Bush" |

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
