# Triple matching report: 904

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Don_Siegel | hasDeathDate | "1991-04-20"^^<http://www.w3.org/2001/XMLSchema#date> |
| Mario_Amendola | hasDeathDate | "1993-12-22"^^<http://www.w3.org/2001/XMLSchema#date> |
| Sexy_Toto | hasDirector | Mario_Amendola |
| Two_Mules_for_Sister_Sara | hasDirector | Don_Siegel |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Don_Siegel | type | Person |
| Don_Siegel | type | NamedIndividual |
| Don_Siegel | label | "Don Siegel" |
| Don_Siegel | altLabel | "Donald Siegel" |
| Mario_Amendola | type | Person |
| Mario_Amendola | type | NamedIndividual |
| Mario_Amendola | label | "Mario Amendola" |
| Sexy_Toto | type | Film |
| Sexy_Toto | type | NamedIndividual |
| Sexy_Toto | label | "Sexy Toto" |
| Two_Mules_for_Sister_Sara | type | Film |
| Two_Mules_for_Sister_Sara | type | NamedIndividual |
| Two_Mules_for_Sister_Sara | label | "Two Mules for Sister Sara" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 17 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.235294 |
| Recall | 1.000000 |
| F1 score | 0.380952 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
