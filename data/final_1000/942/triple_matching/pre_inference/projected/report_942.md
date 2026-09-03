# Triple matching report: 942

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Delmer_Daves | hasBirthDate | "1904-07-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| Demetrius_and_the_Gladiators | hasDirector | Delmer_Daves |
| Lesley_Selander | hasBirthDate | "1900-05-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Riders_of_the_Deadline | hasDirector | Lesley_Selander |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Delmer_Daves | type | Person |
| Delmer_Daves | type | NamedIndividual |
| Delmer_Daves | label | "Delmer Daves" |
| Demetrius_and_the_Gladiators | type | Film |
| Demetrius_and_the_Gladiators | type | NamedIndividual |
| Demetrius_and_the_Gladiators | label | "Demetrius and the Gladiators" |
| Lesley_Selander | type | Person |
| Lesley_Selander | type | NamedIndividual |
| Lesley_Selander | label | "Lesley Selander" |
| Riders_of_the_Deadline | type | Film |
| Riders_of_the_Deadline | type | NamedIndividual |
| Riders_of_the_Deadline | label | "Riders of the Deadline" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 16 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
