# Triple matching report: 205

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| John_Lennon | hasBirthPlace | Liverpool |
| Love | hasPerformer | John_Lennon |

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
| John_Lennon | type | Person |
| John_Lennon | type | NamedIndividual |
| John_Lennon | label | "John Lennon" |
| John_Lennon | altLabel | "John Winston Ono Lennon" |
| Liverpool | type | Place |
| Liverpool | type | NamedIndividual |
| Liverpool | label | "Liverpool" |
| Love | type | CreativeWork |
| Love | type | NamedIndividual |
| Love | label | "Love (John Lennon song)" |
| Love | altLabel | "Love" |

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
