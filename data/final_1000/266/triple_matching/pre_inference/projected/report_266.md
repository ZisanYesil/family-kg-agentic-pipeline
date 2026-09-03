# Triple matching report: 266

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| John_A_McDougald | hasDeathPlace | Palm_Beach |
| Maude_Smith | hasSpouse | John_A_McDougald |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| John_A_McDougald | type | Person |
| John_A_McDougald | type | NamedIndividual |
| John_A_McDougald | label | "John A. McDougald" |
| John_A_McDougald | altLabel | "Bud McDougald" |
| John_A_McDougald | altLabel | "John Angus \"Bud\" McDougald" |
| Maude_Smith | type | Person |
| Maude_Smith | type | NamedIndividual |
| Maude_Smith | label | "Maude Smith" |
| Maude_Smith | altLabel | "Hedley Maude Smith" |
| Maude_Smith | altLabel | "Maude Smith" |
| Palm_Beach | type | Place |
| Palm_Beach | type | NamedIndividual |
| Palm_Beach | label | "Palm Beach, Florida" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
