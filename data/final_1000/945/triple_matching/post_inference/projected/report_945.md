# Triple matching report: 945

# 1. Matched triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Edward_Buzzell | hasDeathDate | "1985-01-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Edward_Buzzell | type | Agent |
| Edward_Buzzell | type | Person |
| Spencer_Gordon_Bennet | hasDeathDate | "1987-10-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| Spencer_Gordon_Bennet | type | Agent |
| Spencer_Gordon_Bennet | type | Person |
| The_Luckiest_Girl_in_the_World | hasCreator | Edward_Buzzell |
| The_Luckiest_Girl_in_the_World | hasDirector | Edward_Buzzell |
| The_Luckiest_Girl_in_the_World | type | Artifact |
| The_Luckiest_Girl_in_the_World | type | CreativeWork |
| The_Luckiest_Girl_in_the_World | type | Film |
| The_Tiger_s_Shadow | hasCreator | Spencer_Gordon_Bennet |
| The_Tiger_s_Shadow | hasDirector | Spencer_Gordon_Bennet |
| The_Tiger_s_Shadow | type | Artifact |
| The_Tiger_s_Shadow | type | CreativeWork |
| The_Tiger_s_Shadow | type | Film |

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
| Edward_Buzzell | hasBirthDate | "1895-11-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Spencer_Gordon_Bennet | hasBirthDate | "1893-01-05"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 16 |
| Union triples in scope | 18 |
| True positives (matched) | 16 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.888889 |
| Recall | 1.000000 |
| F1 score | 0.941176 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
