# Triple matching report: 440

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| John_Manners_Sutton | hasParent | Lord_George_Manners_Sutton |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Lord_George_Manners_Sutton | hasSibling | Lord_Robert_Manners_Sutton |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| John_Manners_Sutton | type | Person |
| John_Manners_Sutton | type | NamedIndividual |
| John_Manners_Sutton | label | "John Manners-Sutton" |
| Lord_George_Manners_Sutton | hasSibling | john_manners_marquess_of_granby |
| Lord_George_Manners_Sutton | type | Person |
| Lord_George_Manners_Sutton | type | NamedIndividual |
| Lord_George_Manners_Sutton | label | "Lord George Manners-Sutton" |
| john_manners_marquess_of_granby | type | Person |
| john_manners_marquess_of_granby | type | NamedIndividual |
| john_manners_marquess_of_granby | label | "John Manners, Marquess of Granby" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
