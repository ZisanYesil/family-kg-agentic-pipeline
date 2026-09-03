# Triple matching report: 540

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| The_Save_the_Children_Fund_Film | hasProducer | Tony_Garnett |
| Tony_Garnett | hasBirthDate | "1936-04-03"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Richard_Gere | hasBirthDate | "1949-08-31"^^<http://www.w3.org/2001/XMLSchema#date> |
| Time_Out_of_Mind_2014_film | hasProducer | Richard_Gere |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| The_Save_the_Children_Fund_Film | type | Film |
| The_Save_the_Children_Fund_Film | type | NamedIndividual |
| The_Save_the_Children_Fund_Film | label | "The Save The Children Fund Film" |
| Time_Out_of_Mind_2014_film | type | Film |
| Time_Out_of_Mind_2014_film | type | NamedIndividual |
| Time_Out_of_Mind_2014_film | label | "Time Out of Mind (2014 Film)" |
| Tony_Garnett | type | Person |
| Tony_Garnett | type | NamedIndividual |
| Tony_Garnett | label | "Tony Garnett" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.181818 |
| Recall | 0.500000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
