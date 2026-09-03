# Triple matching report: 708

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Carl_von_Fersen | hasParent | Hans_Reinhold_von_Fersen |
| Hans_Reinhold_von_Fersen | hasDeathPlace | Stockholm |

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
| Carl_von_Fersen | type | Person |
| Carl_von_Fersen | type | NamedIndividual |
| Carl_von_Fersen | label | "Carl von Fersen" |
| Hans_Reinhold_von_Fersen | type | Person |
| Hans_Reinhold_von_Fersen | type | NamedIndividual |
| Hans_Reinhold_von_Fersen | label | "Hans Reinhold von Fersen" |
| Stockholm | type | Place |
| Stockholm | type | NamedIndividual |
| Stockholm | label | "Stockholm" |

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
