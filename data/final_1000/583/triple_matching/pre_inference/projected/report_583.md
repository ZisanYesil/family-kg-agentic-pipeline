# Triple matching report: 583

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Tim_Russert | hasBirthDate | "1950-05-07"^^<http://www.w3.org/2001/XMLSchema#date> |
| Timothy_John_Russert | hasPresenter | Tim_Russert |

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
| Tim_Russert | type | Person |
| Tim_Russert | type | NamedIndividual |
| Tim_Russert | label | "Tim Russert" |
| Timothy_John_Russert | type | CreativeWork |
| Timothy_John_Russert | type | NamedIndividual |
| Timothy_John_Russert | label | "Tim Russert (talk show)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 8 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
