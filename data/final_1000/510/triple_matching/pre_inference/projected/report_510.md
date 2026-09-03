# Triple matching report: 510

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Antoine_Joseph_Jobert_de_Lamballe | hasBirthDate | "1799-12-17"^^<http://www.w3.org/2001/XMLSchema#date> |
| Antoine_Joseph_Jobert_de_Lamballe | hasDeathDate | "1867-04-19"^^<http://www.w3.org/2001/XMLSchema#date> |
| James_Henry_Dickey_Henderson | hasBirthDate | "1810-07-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| James_Henry_Dickey_Henderson | hasDeathDate | "1885-12-13"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Antoine_Joseph_Jobert_de_Lamballe | type | Person |
| Antoine_Joseph_Jobert_de_Lamballe | type | NamedIndividual |
| Antoine_Joseph_Jobert_de_Lamballe | label | "Antoine Joseph Jobert de Lamballe" |
| James_Henry_Dickey_Henderson | type | Person |
| James_Henry_Dickey_Henderson | type | NamedIndividual |
| James_Henry_Dickey_Henderson | label | "James Henry Dickey Henderson" |

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
