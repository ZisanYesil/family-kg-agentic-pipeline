# Triple matching report: 244

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Forget_About_the_World | hasPerformer | Gabrielle |
| Gabrielle | hasBirthPlace | Hackney |

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
| Forget_About_the_World | type | MusicalWork |
| Forget_About_the_World | type | NamedIndividual |
| Forget_About_the_World | label | "Forget About the World" |
| Gabrielle | hasBirthDate | "1969-07-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| Gabrielle | type | Person |
| Gabrielle | type | NamedIndividual |
| Gabrielle | label | "Gabrielle" |
| Gabrielle | altLabel | "Louisa Gabrielle Bobb" |
| Hackney | type | Place |
| Hackney | type | NamedIndividual |
| Hackney | label | "Hackney, London" |

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
