# Triple matching report: 638

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Francesca_von_Habsburg | hasSpouse | Karl_von_Habsburg |
| Karl_von_Habsburg | hasCountry | Austria |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Austria | type | Country |
| Austria | type | NamedIndividual |
| Austria | label | "Austria" |
| Austria | altLabel | "Austrian" |
| Francesca_von_Habsburg | type | Person |
| Francesca_von_Habsburg | type | NamedIndividual |
| Francesca_von_Habsburg | label | "Francesca von Habsburg" |
| Karl_von_Habsburg | type | Person |
| Karl_von_Habsburg | type | NamedIndividual |
| Karl_von_Habsburg | label | "Karl von Habsburg" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
