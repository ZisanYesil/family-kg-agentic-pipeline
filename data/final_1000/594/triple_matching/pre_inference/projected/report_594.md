# Triple matching report: 594

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Albert_IV_Duke_of_Austria | hasBurialPlace | Stephansdom |
| Joanna_Sophia_of_Bavaria | hasSpouse | Albert_IV_Duke_of_Austria |

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
| Albert_IV_Duke_of_Austria | type | Person |
| Albert_IV_Duke_of_Austria | type | NamedIndividual |
| Albert_IV_Duke_of_Austria | label | "Albert IV, Duke of Austria" |
| Joanna_Sophia_of_Bavaria | type | Person |
| Joanna_Sophia_of_Bavaria | type | NamedIndividual |
| Joanna_Sophia_of_Bavaria | label | "Joanna Sophia of Bavaria" |
| Stephansdom | type | Place |
| Stephansdom | type | NamedIndividual |
| Stephansdom | label | "Ducal Crypt in the Stephansdom, Vienna" |

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
