# Triple matching report: 155

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Alfred_Stieglitz | hasSpouse | Georgia_O_Keeffe |
| Camera_Notes | hasEditor | Alfred_Stieglitz |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Alfred_Stieglitz | type | Person |
| Alfred_Stieglitz | type | NamedIndividual |
| Alfred_Stieglitz | label | "Alfred Stieglitz" |
| Camera_Notes | type | CreativeWork |
| Camera_Notes | type | NamedIndividual |
| Camera_Notes | label | "Camera Notes" |
| Georgia_O_Keeffe | type | Person |
| Georgia_O_Keeffe | type | NamedIndividual |
| Georgia_O_Keeffe | label | "Georgia O'Keeffe" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
