# Triple matching report: 237

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Fred_Keays | hasBirthDate | "1898-07-12"^^<http://www.w3.org/2001/XMLSchema#date> |
| Fred_Keays | hasDeathDate | "1983-06-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_H_Brand | hasBirthDate | "1824-04-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_H_Brand | hasDeathDate | "1891"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Fred_Keays | type | Person |
| Fred_Keays | type | NamedIndividual |
| Fred_Keays | label | "Fred Keays" |
| Fred_Keays | altLabel | "Frederick William Keays" |
| William_H_Brand | type | Person |
| William_H_Brand | type | NamedIndividual |
| William_H_Brand | label | "William H. Brand" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 11 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.363636 |
| Recall | 1.000000 |
| F1 score | 0.533333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
