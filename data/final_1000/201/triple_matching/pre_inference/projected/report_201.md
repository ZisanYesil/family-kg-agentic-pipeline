# Triple matching report: 201

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Francesca_Romana_Serra_Ridgway | hasSpouse | David_Ridgway |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| David_Ridgway | hasBirthPlace | Athens |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| David_Ridgway | type | Person |
| David_Ridgway | type | NamedIndividual |
| David_Ridgway | label | "David Ridgway" |
| Francesca_Romana_Serra_Ridgway | type | Person |
| Francesca_Romana_Serra_Ridgway | type | NamedIndividual |
| Francesca_Romana_Serra_Ridgway | label | "Francesca Ridgway" |
| Francesca_Romana_Serra_Ridgway | altLabel | "Francesca Romana Serra Ridgway" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 9 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.125000 |
| Recall | 0.500000 |
| F1 score | 0.200000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
