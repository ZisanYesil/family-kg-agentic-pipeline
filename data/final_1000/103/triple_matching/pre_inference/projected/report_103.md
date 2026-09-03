# Triple matching report: 103

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Aaron_Aaronsohn | hasBirthDate | "1876-05-21"^^<http://www.w3.org/2001/XMLSchema#date> |
| Aaron_Aaronsohn | hasDeathDate | "1919-05-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| Howard_Purcell | hasBirthDate | "1918-11-10"^^<http://www.w3.org/2001/XMLSchema#date> |
| Howard_Purcell | hasDeathDate | "1981-04-24"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Aaron_Aaronsohn | type | Person |
| Aaron_Aaronsohn | type | NamedIndividual |
| Aaron_Aaronsohn | label | "Aaron Aaronsohn" |
| Howard_Purcell | type | Person |
| Howard_Purcell | type | NamedIndividual |
| Howard_Purcell | label | "Howard Purcell" |

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
