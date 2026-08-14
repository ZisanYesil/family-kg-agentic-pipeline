# Triple matching report: 12

# 1. Matched triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Q1255638 | hasCountry | Q145 |
| Q1255638 | hasCountryOfOrigin | Q145 |
| Q1255638 | type | Artifact |
| Q145 | type | Country |
| Q145 | type | Place |
| Q30 | type | Country |
| Q30 | type | Place |
| Q4345845 | hasCountry | Q30 |
| Q4345845 | hasCountryOfOrigin | Q30 |
| Q4345845 | type | Artifact |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Q1255638 | hasPublicationDate | "2007"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q1255638 | type | CreativeWork |
| Q1255638 | type | Film |
| Q4345845 | hasPublicationDate | "1981"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Q4345845 | type | CreativeWork |
| Q4345845 | type | Film |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 4 |
| Extracted triples in scope | 16 |
| Ground-truth triples in scope | 10 |
| Union triples in scope | 16 |
| True positives (matched) | 10 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.625000 |
| Recall | 1.000000 |
| F1 score | 0.769231 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
