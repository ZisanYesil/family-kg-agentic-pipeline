# Triple matching report: 524

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Catherine_Isabella_Osborne | hasBirthDate | "1818-06-30"^^<http://www.w3.org/2001/XMLSchema#date> |
| Catherine_Isabella_Osborne | hasDeathDate | "1880-06-21"^^<http://www.w3.org/2001/XMLSchema#date> |
| David_Bierens_de_Haan | hasBirthDate | "1822-05-03"^^<http://www.w3.org/2001/XMLSchema#date> |
| David_Bierens_de_Haan | hasDeathDate | "1895-08-12"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Catherine_Isabella_Osborne | type | Person |
| Catherine_Isabella_Osborne | type | NamedIndividual |
| Catherine_Isabella_Osborne | label | "Catherine Isabella Osborne" |
| David_Bierens_de_Haan | type | Person |
| David_Bierens_de_Haan | type | NamedIndividual |
| David_Bierens_de_Haan | label | "David Bierens de Haan" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 10 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.400000 |
| Recall | 1.000000 |
| F1 score | 0.571429 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
