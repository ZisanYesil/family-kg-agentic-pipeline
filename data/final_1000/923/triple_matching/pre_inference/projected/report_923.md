# Triple matching report: 923

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Paul_Foley | hasParent | Thomas_Foley |
| Thomas_Foley | hasCountry | English |

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
| English | type | Country |
| English | type | NamedIndividual |
| English | label | "England" |
| English | altLabel | "English" |
| Paul_Foley | type | Person |
| Paul_Foley | type | NamedIndividual |
| Paul_Foley | label | "Paul Foley" |
| Thomas_Foley | type | Person |
| Thomas_Foley | type | NamedIndividual |
| Thomas_Foley | label | "Thomas Foley" |

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
