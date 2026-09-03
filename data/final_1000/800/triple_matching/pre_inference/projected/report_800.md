# Triple matching report: 800

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| William_S_Burroughs_Jr | hasParent | William_Seward_Burroughs_II |
| William_Seward_Burroughs_II | hasDeathPlace | Lawrence |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Lawrence | type | Place |
| Lawrence | type | NamedIndividual |
| Lawrence | label | "Lawrence, Kansas" |
| William_S_Burroughs_Jr | type | Person |
| William_S_Burroughs_Jr | type | NamedIndividual |
| William_S_Burroughs_Jr | label | "William S. Burroughs Jr." |
| William_S_Burroughs_Jr | altLabel | "Billy Burroughs" |
| William_S_Burroughs_Jr | altLabel | "William S. Burroughs Jr." |
| William_S_Burroughs_Jr | altLabel | "William Seward Burroughs III" |
| William_Seward_Burroughs_II | type | Person |
| William_Seward_Burroughs_II | type | NamedIndividual |
| William_Seward_Burroughs_II | label | "William S. Burroughs" |
| William_Seward_Burroughs_II | altLabel | "William S. Burroughs" |
| William_Seward_Burroughs_II | altLabel | "William Seward Burroughs II" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 16 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.125000 |
| Recall | 1.000000 |
| F1 score | 0.222222 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
