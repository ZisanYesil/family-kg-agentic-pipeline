# Triple matching report: 770

# 1. Matched triples

**Count: 18**

| Subject | Predicate | Object |
|---|---|---|
| Blockade_1938_film | hasCreator | William_Dieterle |
| Blockade_1938_film | hasDirector | William_Dieterle |
| Blockade_1938_film | type | Artifact |
| Blockade_1938_film | type | CreativeWork |
| Blockade_1938_film | type | Film |
| Gerhard_Lamprecht | hasCountry | German |
| Gerhard_Lamprecht | type | Agent |
| Gerhard_Lamprecht | type | Person |
| German | type | Country |
| German | type | Place |
| William_Dieterle | hasCountry | German |
| William_Dieterle | type | Agent |
| William_Dieterle | type | Person |
| Woman_in_the_River | hasCreator | Gerhard_Lamprecht |
| Woman_in_the_River | hasDirector | Gerhard_Lamprecht |
| Woman_in_the_River | type | Artifact |
| Woman_in_the_River | type | CreativeWork |
| Woman_in_the_River | type | Film |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| William_Dieterle | hasCountry | American |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 21 |
| Union triples in scope | 21 |
| True positives (matched) | 18 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 3 |
| Precision | 1.000000 |
| Recall | 0.857143 |
| F1 score | 0.923077 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
