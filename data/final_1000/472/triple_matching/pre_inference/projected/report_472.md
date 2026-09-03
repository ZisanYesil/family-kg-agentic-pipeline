# Triple matching report: 472

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Picturegoer | hasInception | "1911"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Scribner_s_Monthly | hasInception | "1870"^^<http://www.w3.org/2001/XMLSchema#gYear> |

## 2.2 Extracted-only triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| picturegoer_1911 | hasPublicationDate | "1911"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| picturegoer_1911 | type | CreativeWork |
| picturegoer_1911 | type | NamedIndividual |
| picturegoer_1911 | label | "Picturegoer" |
| scribners_monthly_1870 | hasPublicationDate | "1870"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| scribners_monthly_1870 | type | CreativeWork |
| scribners_monthly_1870 | type | NamedIndividual |
| scribners_monthly_1870 | label | "Scribner's Monthly" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 0 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 10 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 8 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
