# Triple matching report: 215

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Albert_Kellogg | hasBirthDate | "1813-12-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Albert_Kellogg | hasDeathDate | "1887-03-31"^^<http://www.w3.org/2001/XMLSchema#date> |
| Johann_Jakob_Schalch | hasBirthDate | "1723-01-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Johann_Jakob_Schalch | hasDeathDate | "1789-08-21"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Albert_Kellogg | type | Person |
| Albert_Kellogg | type | NamedIndividual |
| Albert_Kellogg | label | "Albert Kellogg" |
| Albert_Kellogg | altLabel | "Albert Kellogg" |
| Johann_Jakob_Schalch | type | Person |
| Johann_Jakob_Schalch | type | NamedIndividual |
| Johann_Jakob_Schalch | label | "Johann Jakob Schalch" |
| Johann_Jakob_Schalch | altLabel | "Johann Jakob Schalch" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 12 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.333333 |
| Recall | 1.000000 |
| F1 score | 0.500000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
