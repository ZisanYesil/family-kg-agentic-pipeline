# Triple matching report: 33

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Squire | hasBirthPlace | Kingsbury_London |
| XYZ | hasMember | Chris_Squire |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Chris_Squire | type | Person |
| Chris_Squire | type | NamedIndividual |
| Chris_Squire | label | "Chris Squire" |
| Chris_Squire | altLabel | "Christopher Russell Edward Squire" |
| Kingsbury_London | type | Place |
| Kingsbury_London | type | NamedIndividual |
| Kingsbury_London | label | "Kingsbury, London" |
| XYZ | type | Organization |
| XYZ | type | NamedIndividual |
| XYZ | label | "XYZ" |
| XYZ | altLabel | "XYZ (English band)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
