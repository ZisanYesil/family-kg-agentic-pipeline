# Triple matching report: 655

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Bobby_Previte | hasBirthPlace | Niagara_Falls_New_York |
| The_Coalition_of_the_Willing | hasMember | Bobby_Previte |

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
| Bobby_Previte | type | Person |
| Bobby_Previte | type | NamedIndividual |
| Bobby_Previte | label | "Bobby Previte" |
| Niagara_Falls_New_York | type | Place |
| Niagara_Falls_New_York | type | NamedIndividual |
| Niagara_Falls_New_York | label | "Niagara Falls, New York" |
| The_Coalition_of_the_Willing | type | Organization |
| The_Coalition_of_the_Willing | type | NamedIndividual |
| The_Coalition_of_the_Willing | label | "The Coalition of the Willing" |

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
