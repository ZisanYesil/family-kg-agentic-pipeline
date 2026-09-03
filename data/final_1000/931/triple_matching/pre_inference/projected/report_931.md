# Triple matching report: 931

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Max_Ophüls | hasDeathDate | "1957-03-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Punyakoti | hasDirector | Ravi_Shankar |
| The_Company_s_in_Love | hasDirector | Max_Ophüls |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Ravi_Shankar | hasDeathDate | "2012-12-11"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Max_Ophüls | hasBirthDate | "1902-05-06"^^<http://www.w3.org/2001/XMLSchema#date> |
| Max_Ophüls | type | Person |
| Max_Ophüls | type | NamedIndividual |
| Max_Ophüls | label | "Max Ophüls" |
| Max_Ophüls | altLabel | "Maximillian Oppenheimer" |
| Punyakoti | type | Film |
| Punyakoti | type | NamedIndividual |
| Punyakoti | label | "Punyakoti" |
| Ravi_Shankar | type | Person |
| Ravi_Shankar | type | NamedIndividual |
| Ravi_Shankar | label | "Ravi Shankar V" |
| The_Company_s_in_Love | type | Film |
| The_Company_s_in_Love | type | NamedIndividual |
| The_Company_s_in_Love | label | "The Company's in Love" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 18 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.176471 |
| Recall | 0.750000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
