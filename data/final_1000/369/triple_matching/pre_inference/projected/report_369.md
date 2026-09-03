# Triple matching report: 369

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Pye_Min | hasParent | Thalun |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Thalun | hasSibling | Anaukpetlun |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Pye_Min | type | Person |
| Pye_Min | type | NamedIndividual |
| Pye_Min | label | "Pye Min" |
| Thalun | hasSibling | minye_kyawswa_ii |
| Thalun | type | Person |
| Thalun | type | NamedIndividual |
| Thalun | label | "Thalun" |
| minye_kyawswa_ii | type | Person |
| minye_kyawswa_ii | type | NamedIndividual |
| minye_kyawswa_ii | label | "Minye Kyawswa II" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
