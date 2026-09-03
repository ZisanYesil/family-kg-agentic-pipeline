# Triple matching report: 275

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| David_Ryan_Harris | hasBirthPlace | Evanston_Illinois |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Brand_New_Immortals | hasMember | David_Ryan_Harris |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Brand_New_Immortals | hasFounder | David_Ryan_Harris |
| Brand_New_Immortals | type | Organization |
| Brand_New_Immortals | type | NamedIndividual |
| Brand_New_Immortals | label | "Brand New Immortals" |
| David_Ryan_Harris | type | Person |
| David_Ryan_Harris | type | NamedIndividual |
| David_Ryan_Harris | label | "David Ryan Harris" |
| Evanston_Illinois | type | Place |
| Evanston_Illinois | type | NamedIndividual |
| Evanston_Illinois | label | "Evanston, Illinois" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.090909 |
| Recall | 0.500000 |
| F1 score | 0.153846 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
