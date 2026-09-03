# Triple matching report: 631

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Jay_Marchant | hasDeathPlace | Los_Angeles_County |
| The_Great_Circus_Mystery | hasDirector | Jay_Marchant |

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
| Jay_Marchant | type | Person |
| Jay_Marchant | type | NamedIndividual |
| Jay_Marchant | label | "Jay Marchant" |
| Los_Angeles_County | type | Place |
| Los_Angeles_County | type | NamedIndividual |
| Los_Angeles_County | label | "Los Angeles County, California" |
| The_Great_Circus_Mystery | type | Film |
| The_Great_Circus_Mystery | type | NamedIndividual |
| The_Great_Circus_Mystery | label | "The Great Circus Mystery" |

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
