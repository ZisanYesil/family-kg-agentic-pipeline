# Triple matching report: 48

# 1. Matched triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Mary_Jane_s_Pa | hasCreator | William_Keighley |
| Mary_Jane_s_Pa | hasDirector | William_Keighley |
| Mary_Jane_s_Pa | type | Artifact |
| Mary_Jane_s_Pa | type | CreativeWork |
| Mary_Jane_s_Pa | type | Film |
| New_York | type | Place |
| William_Keighley | hasDeathPlace | New_York |
| William_Keighley | type | Agent |
| William_Keighley | type | Person |

# 2. Unmatched triples

**Total unmatched count: 2**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| William_Keighley | hasBirthDate | "1889-08-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Keighley | hasDeathDate | "1984-06-24"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 11 |
| True positives (matched) | 9 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.818182 |
| Recall | 1.000000 |
| F1 score | 0.900000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
