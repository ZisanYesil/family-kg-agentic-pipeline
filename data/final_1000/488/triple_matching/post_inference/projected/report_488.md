# Triple matching report: 488

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Stefan_Vladislav | type | Agent |
| Stefan_Vladislav | type | Person |
| Stefan_the_First_Crowned | type | Agent |
| Stefan_the_First_Crowned | type | Person |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Serbian_Grand_Principality | type | Country |
| Serbian_Grand_Principality | type | Place |
| Stefan_Vladislav | hasParent | Stefan_the_First_Crowned |
| Stefan_the_First_Crowned | hasChild | Stefan_Vladislav |
| Stefan_the_First_Crowned | hasCountry | Serbian_Grand_Principality |

## 2.2 Extracted-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Stefan_Vladislav | hasChild | Stefan_the_First_Crowned |
| Stefan_the_First_Crowned | hasCountry | serbia |
| Stefan_the_First_Crowned | hasParent | Stefan_Vladislav |
| serbia | type | Country |
| serbia | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 14 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 5 |
| False negatives (ground-truth-only) | 5 |
| Precision | 0.444444 |
| Recall | 0.444444 |
| F1 score | 0.444444 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
