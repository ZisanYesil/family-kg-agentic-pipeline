# Triple matching report: 931

# 1. Matched triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Max_Ophüls | hasDeathDate | "1957-03-26"^^<http://www.w3.org/2001/XMLSchema#date> |
| Max_Ophüls | type | Agent |
| Max_Ophüls | type | Person |
| Punyakoti | hasCreator | Ravi_Shankar |
| Punyakoti | hasDirector | Ravi_Shankar |
| Punyakoti | type | Artifact |
| Punyakoti | type | CreativeWork |
| Punyakoti | type | Film |
| Ravi_Shankar | type | Agent |
| Ravi_Shankar | type | Person |
| The_Company_s_in_Love | hasCreator | Max_Ophüls |
| The_Company_s_in_Love | hasDirector | Max_Ophüls |
| The_Company_s_in_Love | type | Artifact |
| The_Company_s_in_Love | type | CreativeWork |
| The_Company_s_in_Love | type | Film |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Ravi_Shankar | hasDeathDate | "2012-12-11"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Max_Ophüls | hasBirthDate | "1902-05-06"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 16 |
| Union triples in scope | 17 |
| True positives (matched) | 15 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.937500 |
| Recall | 0.937500 |
| F1 score | 0.937500 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
