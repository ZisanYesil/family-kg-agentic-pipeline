# Triple matching report: 145

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Argentine | type | Country |
| Argentine | type | Place |
| If_Dog_Rabbit | hasCountry | American |
| If_Dog_Rabbit | type | Artifact |
| The_Clan_2015_film | hasCountry | Argentine |
| The_Clan_2015_film | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| If_Dog_Rabbit | type | CreativeWork |
| If_Dog_Rabbit | type | Film |
| The_Clan_2015_film | type | CreativeWork |
| The_Clan_2015_film | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 8 |
| Union triples in scope | 12 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.666667 |
| Recall | 1.000000 |
| F1 score | 0.800000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
