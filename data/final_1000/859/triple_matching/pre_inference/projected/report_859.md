# Triple matching report: 859

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| B_S_Ranga | hasDeathDate | "2010-12-12"^^<http://www.w3.org/2001/XMLSchema#date> |
| George_Sherman | hasDeathDate | "1991-03-15"^^<http://www.w3.org/2001/XMLSchema#date> |
| The_Crime_Doctor_s_Courage | hasDirector | George_Sherman |
| Vasantha_Sena_1967_film | hasDirector | B_S_Ranga |

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
| B_S_Ranga | type | Person |
| B_S_Ranga | type | NamedIndividual |
| B_S_Ranga | label | "B. S. Ranga" |
| George_Sherman | type | Person |
| George_Sherman | type | NamedIndividual |
| George_Sherman | label | "George Sherman" |
| The_Crime_Doctor_s_Courage | type | Film |
| The_Crime_Doctor_s_Courage | type | NamedIndividual |
| The_Crime_Doctor_s_Courage | label | "The Crime Doctor's Courage" |
| Vasantha_Sena_1967_film | type | Film |
| Vasantha_Sena_1967_film | type | NamedIndividual |
| Vasantha_Sena_1967_film | label | "Vasantha Sena (1967 film)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 16 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
