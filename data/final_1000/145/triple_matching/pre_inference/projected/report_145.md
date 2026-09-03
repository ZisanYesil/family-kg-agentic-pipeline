# Triple matching report: 145

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| If_Dog_Rabbit | hasCountry | American |
| The_Clan_2015_film | hasCountry | Argentine |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Argentine | type | Country |
| Argentine | type | NamedIndividual |
| Argentine | label | "Argentina" |
| Argentine | altLabel | "Argentine" |
| If_Dog_Rabbit | type | Film |
| If_Dog_Rabbit | type | NamedIndividual |
| If_Dog_Rabbit | label | "If... Dog... Rabbit..." |
| The_Clan_2015_film | type | Film |
| The_Clan_2015_film | type | NamedIndividual |
| The_Clan_2015_film | label | "The Clan (2015 film)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 16 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.125000 |
| Recall | 1.000000 |
| F1 score | 0.222222 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
