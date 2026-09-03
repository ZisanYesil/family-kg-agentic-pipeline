# Triple matching report: 94

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Dortoir_des_grandes | hasDirector | Henri_Decoin |
| Henri_Decoin | hasCountry | French |
| Is_Paris_Burning_film | hasDirector | René_Clément |
| René_Clément | hasCountry | French |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| Dortoir_des_grandes | type | Film |
| Dortoir_des_grandes | type | NamedIndividual |
| Dortoir_des_grandes | label | "Dortoir des grandes" |
| French | type | Country |
| French | type | NamedIndividual |
| French | label | "France" |
| French | altLabel | "French" |
| Henri_Decoin | type | Person |
| Henri_Decoin | type | NamedIndividual |
| Henri_Decoin | label | "Henri Decoin" |
| Is_Paris_Burning_film | type | Film |
| Is_Paris_Burning_film | type | NamedIndividual |
| Is_Paris_Burning_film | label | "Is Paris Burning?" |
| René_Clément | type | Person |
| René_Clément | type | NamedIndividual |
| René_Clément | label | "René Clément" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 20 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
