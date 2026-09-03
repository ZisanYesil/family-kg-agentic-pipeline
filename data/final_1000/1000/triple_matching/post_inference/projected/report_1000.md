# Triple matching report: 1000

# 1. Matched triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Apne_Dam_Par | hasCreator | Arshad_Khan |
| Apne_Dam_Par | hasDirector | Arshad_Khan |
| Apne_Dam_Par | type | Artifact |
| Apne_Dam_Par | type | CreativeWork |
| Apne_Dam_Par | type | Film |
| Arshad_Khan | type | Agent |
| Arshad_Khan | type | Person |
| Cela_s_appelle_l_aurore | hasCreator | Luis_Buñuel |
| Cela_s_appelle_l_aurore | hasDirector | Luis_Buñuel |
| Cela_s_appelle_l_aurore | type | Artifact |
| Cela_s_appelle_l_aurore | type | CreativeWork |
| Cela_s_appelle_l_aurore | type | Film |
| Luis_Buñuel | hasBirthDate | "1900-02-22"^^<http://www.w3.org/2001/XMLSchema#date> |
| Luis_Buñuel | type | Agent |
| Luis_Buñuel | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Arshad_Khan_cricketer | hasBirthDate | "1971-03-22"^^<http://www.w3.org/2001/XMLSchema#date> |
| Arshad_Khan_cricketer | type | Agent |
| Arshad_Khan_cricketer | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Arshad_Khan | hasBirthDate | "1971-03-22"^^<http://www.w3.org/2001/XMLSchema#date> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 18 |
| Union triples in scope | 19 |
| True positives (matched) | 15 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.937500 |
| Recall | 0.833333 |
| F1 score | 0.882353 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
