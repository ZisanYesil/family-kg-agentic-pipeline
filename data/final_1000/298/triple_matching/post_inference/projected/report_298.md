# Triple matching report: 298

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Borys_Lankosz | hasEducatedAt | National_Film_School_in_Łódź |
| Borys_Lankosz | type | Agent |
| Borys_Lankosz | type | Person |
| National_Film_School_in_Łódź | type | Agent |
| National_Film_School_in_Łódź | type | EducationalInstitution |
| National_Film_School_in_Łódź | type | Organization |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Rewers | hasCreator | Borys_Lankosz |
| Rewers | hasDirector | Borys_Lankosz |
| Rewers | type | Artifact |
| Rewers | type | CreativeWork |
| Rewers | type | Film |

## 2.2 Extracted-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| reverse_film | hasCreator | Borys_Lankosz |
| reverse_film | hasDirector | Borys_Lankosz |
| reverse_film | type | Artifact |
| reverse_film | type | CreativeWork |
| reverse_film | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 11 |
| Union triples in scope | 16 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 5 |
| False negatives (ground-truth-only) | 5 |
| Precision | 0.545455 |
| Recall | 0.545455 |
| F1 score | 0.545455 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
