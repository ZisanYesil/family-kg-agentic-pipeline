# Triple matching report: 661

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Cyril_Hanouna | hasBirthPlace | Paris |
| It_s_Only_TV | hasCreator | Cyril_Hanouna |

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
| Cyril_Hanouna | hasBirthDate | "1974-09-23"^^<http://www.w3.org/2001/XMLSchema#date> |
| Cyril_Hanouna | type | Person |
| Cyril_Hanouna | type | NamedIndividual |
| Cyril_Hanouna | label | "Cyril Hanouna" |
| Cyril_Hanouna | altLabel | "Cyril Valéry Hanouna" |
| It_s_Only_TV | type | CreativeWork |
| It_s_Only_TV | type | NamedIndividual |
| It_s_Only_TV | label | "It's Only TV" |
| It_s_Only_TV | altLabel | "Touche pas à mon poste !" |
| Paris | type | Place |
| Paris | type | NamedIndividual |
| Paris | label | "Paris" |

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
