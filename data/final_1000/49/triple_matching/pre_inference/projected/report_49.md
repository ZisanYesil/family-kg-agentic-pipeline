# Triple matching report: 49

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Franz_Waxman | hasCountry | German |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Count_Your_Blessings | hasComposer | Franz_Waxman |

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Count_Your_Blessings | type | Film |
| Count_Your_Blessings | type | NamedIndividual |
| Count_Your_Blessings | label | "Count Your Blessings (1959 film)" |
| Franz_Waxman | hasCountry | united_states |
| Franz_Waxman | type | Person |
| Franz_Waxman | type | NamedIndividual |
| Franz_Waxman | label | "Franz Waxman" |
| German | type | Country |
| German | type | NamedIndividual |
| German | label | "Germany" |
| German | altLabel | "German" |
| united_states | type | Country |
| united_states | type | NamedIndividual |
| united_states | label | "United States" |
| united_states | altLabel | "American" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 17 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.062500 |
| Recall | 0.500000 |
| F1 score | 0.111111 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
