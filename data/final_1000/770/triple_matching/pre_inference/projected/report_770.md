# Triple matching report: 770

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Blockade_1938_film | hasDirector | William_Dieterle |
| Gerhard_Lamprecht | hasCountry | German |
| William_Dieterle | hasCountry | German |
| Woman_in_the_River | hasDirector | Gerhard_Lamprecht |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| William_Dieterle | hasCountry | American |

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Blockade_1938_film | type | Film |
| Blockade_1938_film | type | NamedIndividual |
| Blockade_1938_film | label | "Blockade (1938 film)" |
| Gerhard_Lamprecht | type | Person |
| Gerhard_Lamprecht | type | NamedIndividual |
| Gerhard_Lamprecht | label | "Gerhard Lamprecht" |
| German | type | Country |
| German | type | NamedIndividual |
| German | label | "Germany" |
| German | altLabel | "German" |
| William_Dieterle | type | Person |
| William_Dieterle | type | NamedIndividual |
| William_Dieterle | label | "William Dieterle" |
| Woman_in_the_River | type | Film |
| Woman_in_the_River | type | NamedIndividual |
| Woman_in_the_River | label | "Woman in the River" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 5 |
| Union triples in scope | 21 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.200000 |
| Recall | 0.800000 |
| F1 score | 0.320000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
