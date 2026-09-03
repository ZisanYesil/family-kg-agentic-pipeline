# Triple matching report: 799

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| George_Bernhard_of_Anhalt_Dessau | hasParent | Landgravine_Amalie_of_Hesse_Homburg |
| Princess_Amalie_of_Hesse_Homburg | hasBirthPlace | Bad_Homburg_vor_der_Höhe |

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Bad_Homburg_vor_der_Höhe | type | Place |
| Bad_Homburg_vor_der_Höhe | type | NamedIndividual |
| Bad_Homburg_vor_der_Höhe | label | "Bad Homburg vor der Höhe" |
| George_Bernhard_of_Anhalt_Dessau | hasParent | amelie_of_hesse_homburg |
| George_Bernhard_of_Anhalt_Dessau | type | Person |
| George_Bernhard_of_Anhalt_Dessau | type | NamedIndividual |
| George_Bernhard_of_Anhalt_Dessau | label | "George Bernhard of Anhalt-Dessau" |
| amelie_of_hesse_homburg | hasBirthPlace | Bad_Homburg_vor_der_Höhe |
| amelie_of_hesse_homburg | type | Person |
| amelie_of_hesse_homburg | type | NamedIndividual |
| amelie_of_hesse_homburg | label | "Amalie of Hesse-Homburg" |
| amelie_of_hesse_homburg | altLabel | "Christiane Amalie, Landgräfin von Hessen-Homburg" |
| amelie_of_hesse_homburg | altLabel | "Princess and Landgravine Christiane Amalie of Hesse-Homburg" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
