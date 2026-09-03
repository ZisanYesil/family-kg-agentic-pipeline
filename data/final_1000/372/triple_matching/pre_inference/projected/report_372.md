# Triple matching report: 372

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| James_Scudamore_3rd_Viscount_Scudamore | hasParent | John_Scudamore_2nd_Viscount_Scudamore |
| John_Scudamore_2nd_Viscount_Scudamore | hasParent | Jane_Bennet |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| James_Scudamore_3rd_Viscount_Scudamore | type | Person |
| James_Scudamore_3rd_Viscount_Scudamore | type | NamedIndividual |
| James_Scudamore_3rd_Viscount_Scudamore | label | "James Scudamore, 3rd Viscount Scudamore" |
| Jane_Bennet | type | Person |
| Jane_Bennet | type | NamedIndividual |
| Jane_Bennet | label | "Jane Bennet" |
| John_Scudamore_2nd_Viscount_Scudamore | type | Person |
| John_Scudamore_2nd_Viscount_Scudamore | type | NamedIndividual |
| John_Scudamore_2nd_Viscount_Scudamore | label | "John Scudamore, 2nd Viscount Scudamore" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
