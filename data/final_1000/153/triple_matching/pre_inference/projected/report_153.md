# Triple matching report: 153

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Gå_och_göm_dig_Åke_Tråk | hasPerformer | Mona_Wessman |
| Mona_Wessman | hasCountry | Sweden |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Gå_och_göm_dig_Åke_Tråk | type | MusicalWork |
| Gå_och_göm_dig_Åke_Tråk | type | NamedIndividual |
| Gå_och_göm_dig_Åke_Tråk | label | "Gå och göm dig, Åke Tråk" |
| Mona_Wessman | type | Person |
| Mona_Wessman | type | NamedIndividual |
| Mona_Wessman | label | "Mona Wessman" |
| Sweden | type | Country |
| Sweden | type | NamedIndividual |
| Sweden | label | "Sweden" |
| Sweden | altLabel | "Swedish" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
