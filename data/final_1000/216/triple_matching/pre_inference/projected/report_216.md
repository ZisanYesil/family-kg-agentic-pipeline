# Triple matching report: 216

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Hannes_Stöhr | hasEducatedAt | Deutsche_Film_und_Fernsehakademie_Berlin |
| One_Day_in_Europe | hasDirector | Hannes_Stöhr |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Deutsche_Film_und_Fernsehakademie_Berlin | type | EducationalInstitution |
| Deutsche_Film_und_Fernsehakademie_Berlin | type | NamedIndividual |
| Deutsche_Film_und_Fernsehakademie_Berlin | label | "Deutsche Film- und Fernsehakademie Berlin" |
| Hannes_Stöhr | type | Person |
| Hannes_Stöhr | type | NamedIndividual |
| Hannes_Stöhr | label | "Hannes Stöhr" |
| One_Day_in_Europe | type | Film |
| One_Day_in_Europe | type | NamedIndividual |
| One_Day_in_Europe | label | "One Day in Europe" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
