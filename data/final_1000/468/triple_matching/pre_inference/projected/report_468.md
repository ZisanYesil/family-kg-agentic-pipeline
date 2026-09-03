# Triple matching report: 468

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Alain_Gomis | hasCountry | French |
| Alain_Gomis | hasCountry | Senegalese |
| Benoît_Jacquot | hasCountry | French |
| Félicité_2017_film | hasDirector | Alain_Gomis |
| Villa_Amalia_film | hasDirector | Benoît_Jacquot |

# 2. Unmatched triples

**Total unmatched count: 20**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 20**

| Subject | Predicate | Object |
|---|---|---|
| Alain_Gomis | type | Person |
| Alain_Gomis | type | NamedIndividual |
| Alain_Gomis | label | "Alain Gomis" |
| Benoît_Jacquot | type | Person |
| Benoît_Jacquot | type | NamedIndividual |
| Benoît_Jacquot | label | "Benoît Jacquot" |
| French | type | Country |
| French | type | NamedIndividual |
| French | label | "France" |
| French | altLabel | "French" |
| Félicité_2017_film | type | Film |
| Félicité_2017_film | type | NamedIndividual |
| Félicité_2017_film | label | "Félicité" |
| Senegalese | type | Country |
| Senegalese | type | NamedIndividual |
| Senegalese | label | "Senegal" |
| Senegalese | altLabel | "Senegalese" |
| Villa_Amalia_film | type | Film |
| Villa_Amalia_film | type | NamedIndividual |
| Villa_Amalia_film | label | "Villa Amalia" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 6 |
| Extracted triples in scope | 25 |
| Ground-truth triples in scope | 5 |
| Union triples in scope | 25 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 20 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
