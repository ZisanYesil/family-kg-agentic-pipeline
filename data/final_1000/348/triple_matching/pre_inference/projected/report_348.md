# Triple matching report: 348

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Beyond_Rangoon | hasDirector | John_Boorman |
| David_Lean | hasCountry | British |
| John_Boorman | hasCountry | British |
| Ryan_s_Daughter | hasDirector | David_Lean |

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
| Beyond_Rangoon | type | Film |
| Beyond_Rangoon | type | NamedIndividual |
| Beyond_Rangoon | label | "Beyond Rangoon" |
| British | type | Country |
| British | type | NamedIndividual |
| British | label | "United Kingdom" |
| British | altLabel | "English" |
| David_Lean | type | Person |
| David_Lean | type | NamedIndividual |
| David_Lean | label | "David Lean" |
| John_Boorman | type | Person |
| John_Boorman | type | NamedIndividual |
| John_Boorman | label | "John Boorman" |
| Ryan_s_Daughter | type | Film |
| Ryan_s_Daughter | type | NamedIndividual |
| Ryan_s_Daughter | label | "Ryan's Daughter" |

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
