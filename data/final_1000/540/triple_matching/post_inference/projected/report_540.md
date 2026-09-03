# Triple matching report: 540

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| The_Save_the_Children_Fund_Film | hasProducer | Tony_Garnett |
| The_Save_the_Children_Fund_Film | type | Artifact |
| The_Save_the_Children_Fund_Film | type | CreativeWork |
| Time_Out_of_Mind_2014_film | type | Artifact |
| Time_Out_of_Mind_2014_film | type | CreativeWork |
| Tony_Garnett | hasBirthDate | "1936-04-03"^^<http://www.w3.org/2001/XMLSchema#date> |
| Tony_Garnett | type | Agent |
| Tony_Garnett | type | Person |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Richard_Gere | hasBirthDate | "1949-08-31"^^<http://www.w3.org/2001/XMLSchema#date> |
| Richard_Gere | type | Agent |
| Richard_Gere | type | Person |
| Time_Out_of_Mind_2014_film | hasProducer | Richard_Gere |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| The_Save_the_Children_Fund_Film | type | Film |
| Time_Out_of_Mind_2014_film | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 12 |
| Union triples in scope | 14 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 4 |
| Precision | 0.800000 |
| Recall | 0.666667 |
| F1 score | 0.727273 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
