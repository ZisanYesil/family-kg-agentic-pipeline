# Triple matching report: 139

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Ed_Blackwell | hasBirthPlace | New_Orleans_Louisiana |
| Old_and_New_Dreams | hasMember | Ed_Blackwell |

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
| Ed_Blackwell | type | Person |
| Ed_Blackwell | type | NamedIndividual |
| Ed_Blackwell | label | "Ed Blackwell" |
| Ed_Blackwell | altLabel | "Edward Joseph Blackwell" |
| New_Orleans_Louisiana | type | Place |
| New_Orleans_Louisiana | type | NamedIndividual |
| New_Orleans_Louisiana | label | "New Orleans, Louisiana" |
| Old_and_New_Dreams | type | Organization |
| Old_and_New_Dreams | type | NamedIndividual |
| Old_and_New_Dreams | label | "Old and New Dreams" |

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
