# Triple matching report: 154

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Don_t_Let_Me_Down | hasPerformer | Leona_Lewis |
| Leona_Lewis | hasBirthPlace | London |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Don_t_Let_Me_Down | type | CreativeWork |
| Don_t_Let_Me_Down | type | NamedIndividual |
| Don_t_Let_Me_Down | label | "Don't Let Me Down (Leona Lewis song)" |
| Leona_Lewis | type | Person |
| Leona_Lewis | type | NamedIndividual |
| Leona_Lewis | label | "Leona Lewis" |
| Leona_Lewis | altLabel | "Leona Louise Lewis" |
| London | type | Place |
| London | type | NamedIndividual |
| London | label | "London Borough of Islington" |
| London | altLabel | "Islington" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
