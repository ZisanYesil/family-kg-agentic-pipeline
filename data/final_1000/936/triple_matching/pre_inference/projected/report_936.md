# Triple matching report: 936

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Harb_ibn_Umayya | hasParent | Umayya_ibn_Abd_Shams |
| Harith_ibn_Harb | hasParent | Harb_ibn_Umayya |

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
| Harb_ibn_Umayya | type | Person |
| Harb_ibn_Umayya | type | NamedIndividual |
| Harb_ibn_Umayya | label | "Harb ibn Umayya" |
| Harith_ibn_Harb | type | Person |
| Harith_ibn_Harb | type | NamedIndividual |
| Harith_ibn_Harb | label | "Harith ibn Harb" |
| Umayya_ibn_Abd_Shams | type | Person |
| Umayya_ibn_Abd_Shams | type | NamedIndividual |
| Umayya_ibn_Abd_Shams | label | "Umayya ibn Abd Shams" |

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
