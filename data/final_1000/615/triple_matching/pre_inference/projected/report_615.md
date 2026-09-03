# Triple matching report: 615

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Christopher_Columbus_The_Enigma | hasDirector | Manoel_de_Oliveira |
| Manoel_de_Oliveira | hasBirthPlace | Porto |

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
| Christopher_Columbus_The_Enigma | type | Film |
| Christopher_Columbus_The_Enigma | type | NamedIndividual |
| Christopher_Columbus_The_Enigma | label | "Christopher Columbus – The Enigma" |
| Christopher_Columbus_The_Enigma | altLabel | "Cristóvão Colombo - O Enigma" |
| Manoel_de_Oliveira | type | Person |
| Manoel_de_Oliveira | type | NamedIndividual |
| Manoel_de_Oliveira | label | "Manoel de Oliveira" |
| Manoel_de_Oliveira | altLabel | "Manoel Cândido Pinto de Oliveira" |
| Porto | type | Place |
| Porto | type | NamedIndividual |
| Porto | label | "Cedofeita, Porto" |

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
