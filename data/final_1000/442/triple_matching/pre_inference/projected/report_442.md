# Triple matching report: 442

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Eleanor_de_Clare | hasBirthPlace | Caerphilly |
| Hugh_le_Despenser | hasParent | Eleanor_de_Clare |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Caerphilly | type | Place |
| Caerphilly | type | NamedIndividual |
| Caerphilly | label | "Caerphilly Castle" |
| Caerphilly | altLabel | "Caerphilly Castle" |
| Eleanor_de_Clare | type | Person |
| Eleanor_de_Clare | type | NamedIndividual |
| Eleanor_de_Clare | label | "Eleanor de Clare" |
| Eleanor_de_Clare | altLabel | "Eleanor de Clare" |
| Hugh_le_Despenser | type | Person |
| Hugh_le_Despenser | type | NamedIndividual |
| Hugh_le_Despenser | label | "Hugh Le Despenser, Baron Le Despenser (1338)" |
| Hugh_le_Despenser | altLabel | "Hugh Le Despenser, Baron Le Despenser (1338)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.142857 |
| Recall | 1.000000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
