# Triple matching report: 48

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Mary_Jane_s_Pa | hasDirector | William_Keighley |
| William_Keighley | hasDeathPlace | New_York |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Mary_Jane_s_Pa | type | Film |
| Mary_Jane_s_Pa | type | NamedIndividual |
| Mary_Jane_s_Pa | label | "Mary Jane's Pa" |
| New_York | type | Place |
| New_York | type | NamedIndividual |
| New_York | label | "New York, New York" |
| William_Keighley | hasBirthDate | "1889-08-04"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Keighley | hasDeathDate | "1984-06-24"^^<http://www.w3.org/2001/XMLSchema#date> |
| William_Keighley | type | Person |
| William_Keighley | type | NamedIndividual |
| William_Keighley | label | "William Keighley" |
| William_Keighley | altLabel | "William Jackson Keighley" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.142857 |
| Recall | 1.000000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
