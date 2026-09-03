# Triple matching report: 160

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Fanfare_of_Love | type | Artifact |
| French | type | Country |
| French | type | Place |
| Guilty_2011_film | hasCountry | French |
| Guilty_2011_film | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 8**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Fanfare_of_Love | hasCountry | French |

## 2.2 Extracted-only triples

**Count: 7**

| Subject | Predicate | Object |
|---|---|---|
| Fanfare_of_Love | hasCountry | west_germany |
| Fanfare_of_Love | type | CreativeWork |
| Fanfare_of_Love | type | Film |
| Guilty_2011_film | type | CreativeWork |
| Guilty_2011_film | type | Film |
| west_germany | type | Country |
| west_germany | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 6 |
| Union triples in scope | 13 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 7 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.416667 |
| Recall | 0.833333 |
| F1 score | 0.555556 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
