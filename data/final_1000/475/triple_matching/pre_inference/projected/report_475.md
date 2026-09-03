# Triple matching report: 475

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Agnes_Ballard | hasBirthDate | "1877-09-14"^^<http://www.w3.org/2001/XMLSchema#date> |
| Agnes_Ballard | hasDeathDate | "1969-11-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Reginald_Morse | hasBirthDate | "1874-08-30"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Reginald_Morse | hasDeathDate | "1939-11-11"^^<http://www.w3.org/2001/XMLSchema#date> |

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
| Agnes_Ballard | type | Person |
| Agnes_Ballard | type | NamedIndividual |
| Agnes_Ballard | label | "Agnes Ballard" |
| William_Reginald_Morse | type | Person |
| William_Reginald_Morse | type | NamedIndividual |
| William_Reginald_Morse | label | "William Reginald Morse" |

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
