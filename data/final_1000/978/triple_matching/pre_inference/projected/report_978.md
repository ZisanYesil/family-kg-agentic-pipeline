# Triple matching report: 978

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| David_Fennario | hasBirthDate | "1947-04-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Peter_Emanuel_Falck | hasBirthDate | "1952-07-15"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| David_Fennario | type | Person |
| David_Fennario | type | NamedIndividual |
| David_Fennario | label | "David Fennario" |
| David_Fennario | altLabel | "David William Fennario" |
| Peter_Emanuel_Falck | type | Person |
| Peter_Emanuel_Falck | type | NamedIndividual |
| Peter_Emanuel_Falck | label | "Peter Emanuel Falck" |
| Peter_Emanuel_Falck | altLabel | "John Peter Emanuel Falck" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
