# Triple matching report: 684

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Sigismund_II_Augustus | hasParent | Bona_Sforza |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Bona_Sforza | hasCountry | Duchy_of_Milan |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Bona_Sforza | hasCountry | italy |
| Bona_Sforza | type | Person |
| Bona_Sforza | type | NamedIndividual |
| Bona_Sforza | label | "Bona Sforza" |
| Sigismund_II_Augustus | type | Person |
| Sigismund_II_Augustus | type | NamedIndividual |
| Sigismund_II_Augustus | label | "Sigismund II Augustus" |
| italy | type | Country |
| italy | type | NamedIndividual |
| italy | label | "Italy" |
| italy | altLabel | "Italian" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
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
