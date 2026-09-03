# Triple matching report: 51

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Orelsan | hasBirthPlace | Alençon |
| Suicide_social | hasPerformer | Orelsan |

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
| Alençon | type | Place |
| Alençon | type | NamedIndividual |
| Alençon | label | "Alençon, Orne" |
| Orelsan | type | Person |
| Orelsan | type | NamedIndividual |
| Orelsan | label | "Orelsan" |
| Orelsan | altLabel | "Aurélien Cotentin" |
| Suicide_social | type | MusicalWork |
| Suicide_social | type | NamedIndividual |
| Suicide_social | label | "Suicide social" |

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
