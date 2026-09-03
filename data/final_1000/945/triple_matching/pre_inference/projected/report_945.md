# Triple matching report: 945

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Edward_Buzzell | hasDeathDate | "1985-01-11"^^<http://www.w3.org/2001/XMLSchema#date> |
| Spencer_Gordon_Bennet | hasDeathDate | "1987-10-08"^^<http://www.w3.org/2001/XMLSchema#date> |
| The_Luckiest_Girl_in_the_World | hasDirector | Edward_Buzzell |
| The_Tiger_s_Shadow | hasDirector | Spencer_Gordon_Bennet |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Edward_Buzzell | hasBirthDate | "1895-11-13"^^<http://www.w3.org/2001/XMLSchema#date> |
| Edward_Buzzell | type | Person |
| Edward_Buzzell | type | NamedIndividual |
| Edward_Buzzell | label | "Edward Buzzell" |
| Spencer_Gordon_Bennet | hasBirthDate | "1893-01-05"^^<http://www.w3.org/2001/XMLSchema#date> |
| Spencer_Gordon_Bennet | type | Person |
| Spencer_Gordon_Bennet | type | NamedIndividual |
| Spencer_Gordon_Bennet | label | "Spencer Gordon Bennet" |
| The_Luckiest_Girl_in_the_World | type | Film |
| The_Luckiest_Girl_in_the_World | type | NamedIndividual |
| The_Luckiest_Girl_in_the_World | label | "The Luckiest Girl in the World" |
| The_Tiger_s_Shadow | type | Film |
| The_Tiger_s_Shadow | type | NamedIndividual |
| The_Tiger_s_Shadow | label | "The Tiger's Shadow" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 18 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.222222 |
| Recall | 1.000000 |
| F1 score | 0.363636 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
