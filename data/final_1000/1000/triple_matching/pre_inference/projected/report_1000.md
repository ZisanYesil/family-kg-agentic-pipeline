# Triple matching report: 1000

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Apne_Dam_Par | hasDirector | Arshad_Khan |
| Cela_s_appelle_l_aurore | hasDirector | Luis_Buñuel |
| Luis_Buñuel | hasBirthDate | "1900-02-22"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Arshad_Khan_cricketer | hasBirthDate | "1971-03-22"^^<http://www.w3.org/2001/XMLSchema#date> |

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Apne_Dam_Par | type | Film |
| Apne_Dam_Par | type | NamedIndividual |
| Apne_Dam_Par | label | "Apne Dam Par" |
| Arshad_Khan | hasBirthDate | "1971-03-22"^^<http://www.w3.org/2001/XMLSchema#date> |
| Arshad_Khan | type | Person |
| Arshad_Khan | type | NamedIndividual |
| Arshad_Khan | label | "Arshad Khan" |
| Cela_s_appelle_l_aurore | type | Film |
| Cela_s_appelle_l_aurore | type | NamedIndividual |
| Cela_s_appelle_l_aurore | label | "Cela s'appelle l'aurore" |
| Luis_Buñuel | type | Person |
| Luis_Buñuel | type | NamedIndividual |
| Luis_Buñuel | label | "Luis Buñuel" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 17 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.187500 |
| Recall | 0.750000 |
| F1 score | 0.300000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
