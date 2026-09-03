# Triple matching report: 31

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Leona_Lewis | hasBirthPlace | London |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| I_See_You | hasPerformer | Leona_Lewis |

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Leona_Lewis | type | Person |
| Leona_Lewis | type | NamedIndividual |
| Leona_Lewis | label | "Leona Lewis" |
| Leona_Lewis | altLabel | "Leona Louise Lewis" |
| London | type | Place |
| London | type | NamedIndividual |
| London | label | "Islington, London" |
| London | altLabel | "London Borough of Islington" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 9 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.111111 |
| Recall | 0.500000 |
| F1 score | 0.181818 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
