# Triple matching report: 799

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Bad_Homburg_vor_der_Höhe | type | Place |
| George_Bernhard_of_Anhalt_Dessau | type | Agent |
| George_Bernhard_of_Anhalt_Dessau | type | Person |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| George_Bernhard_of_Anhalt_Dessau | hasParent | Landgravine_Amalie_of_Hesse_Homburg |
| Landgravine_Amalie_of_Hesse_Homburg | hasChild | George_Bernhard_of_Anhalt_Dessau |
| Landgravine_Amalie_of_Hesse_Homburg | type | Agent |
| Landgravine_Amalie_of_Hesse_Homburg | type | Person |
| Princess_Amalie_of_Hesse_Homburg | hasBirthPlace | Bad_Homburg_vor_der_Höhe |
| Princess_Amalie_of_Hesse_Homburg | type | Agent |
| Princess_Amalie_of_Hesse_Homburg | type | Person |

## 2.2 Extracted-only triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| George_Bernhard_of_Anhalt_Dessau | hasParent | amelie_of_hesse_homburg |
| amelie_of_hesse_homburg | hasBirthPlace | Bad_Homburg_vor_der_Höhe |
| amelie_of_hesse_homburg | hasChild | George_Bernhard_of_Anhalt_Dessau |
| amelie_of_hesse_homburg | type | Agent |
| amelie_of_hesse_homburg | type | Person |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 15 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 5 |
| False negatives (ground-truth-only) | 7 |
| Precision | 0.375000 |
| Recall | 0.300000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
