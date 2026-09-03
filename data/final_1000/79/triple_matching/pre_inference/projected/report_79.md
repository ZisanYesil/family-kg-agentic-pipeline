# Triple matching report: 79

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| A_French_Gigolo | hasDirector | Josiane_Balasko |
| Josiane_Balasko | hasCountry | French |
| René_Barberis | hasCountry | French |
| Temptation_1929_film | hasDirector | René_Barberis |

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
| A_French_Gigolo | type | Film |
| A_French_Gigolo | type | NamedIndividual |
| A_French_Gigolo | label | "A French Gigolo" |
| French | type | Country |
| French | type | NamedIndividual |
| French | label | "France" |
| French | altLabel | "French" |
| Josiane_Balasko | type | Person |
| Josiane_Balasko | type | NamedIndividual |
| Josiane_Balasko | label | "Josiane Balasko" |
| René_Barberis | type | Person |
| René_Barberis | type | NamedIndividual |
| René_Barberis | label | "René Barberis" |
| Temptation_1929_film | type | Film |
| Temptation_1929_film | type | NamedIndividual |
| Temptation_1929_film | label | "Temptation (1929 film)" |

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
