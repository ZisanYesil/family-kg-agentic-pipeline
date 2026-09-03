# Triple matching report: 844

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gillian_Blake | hasSpouse | Peter_Whitbread |
| Peter_Whitbread | hasEducatedAt | Gresham_s_School |

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
| Gillian_Blake | type | Person |
| Gillian_Blake | type | NamedIndividual |
| Gillian_Blake | label | "Gillian Blake" |
| Gresham_s_School | type | EducationalInstitution |
| Gresham_s_School | type | NamedIndividual |
| Gresham_s_School | label | "Gresham's School" |
| Gresham_s_School | altLabel | "Gresham's School, Holt, Norfolk" |
| Peter_Whitbread | type | Person |
| Peter_Whitbread | type | NamedIndividual |
| Peter_Whitbread | label | "Peter Whitbread" |

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
