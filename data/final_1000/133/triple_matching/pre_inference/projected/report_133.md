# Triple matching report: 133

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Hugo_Chávez | hasBirthPlace | Sabaneta |
| Universidad_Militar_Bolivariana_de_Venezuela | hasFounder | Hugo_Chávez |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Hugo_Chávez | type | Person |
| Hugo_Chávez | type | NamedIndividual |
| Hugo_Chávez | label | "Hugo Chávez" |
| Hugo_Chávez | altLabel | "Hugo Rafael Chávez Frías" |
| Sabaneta | type | Place |
| Sabaneta | type | NamedIndividual |
| Sabaneta | label | "Sabaneta, Barinas" |
| Universidad_Militar_Bolivariana_de_Venezuela | type | EducationalInstitution |
| Universidad_Militar_Bolivariana_de_Venezuela | type | NamedIndividual |
| Universidad_Militar_Bolivariana_de_Venezuela | label | "Bolivarian Military University of Venezuela" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
