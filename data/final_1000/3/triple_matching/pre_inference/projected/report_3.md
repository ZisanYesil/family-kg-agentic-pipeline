# Triple matching report: 3

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jean_Martin | hasSpouse | William_Black |
| William_Black | hasDeathDate | "1983"^^<http://www.w3.org/2001/XMLSchema#gYear> |

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
| Jean_Martin | type | Person |
| Jean_Martin | type | NamedIndividual |
| Jean_Martin | label | "Jean Martin" |
| Jean_Martin | altLabel | "Jean Martin (singer)" |
| William_Black | type | Person |
| William_Black | type | NamedIndividual |
| William_Black | label | "William Black" |
| William_Black | altLabel | "William Black (businessman)" |

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
