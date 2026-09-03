# Triple matching report: 628

# 1. Matched triples

**Count: 8**

| Subject | Predicate | Object |
|---|---|---|
| Aleksei_Saltykov | type | Agent |
| Aleksei_Saltykov | type | Person |
| People_s_Artist_of_the_RSFSR | type | Award |
| Pugachev | hasCreator | Aleksei_Saltykov |
| Pugachev | hasDirector | Aleksei_Saltykov |
| Pugachev | type | Artifact |
| Pugachev | type | CreativeWork |
| Pugachev | type | Film |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Aleksey_Aleksandrovich_Saltykov | hasAwardReceived | People_s_Artist_of_the_RSFSR |

## 2.2 Extracted-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Aleksei_Saltykov | hasAwardReceived | People_s_Artist_of_the_RSFSR |
| Pugachev | hasPublicationDate | "1978"^^<http://www.w3.org/2001/XMLSchema#gYear> |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 11 |
| True positives (matched) | 8 |
| False positives (extracted-only) | 2 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.800000 |
| Recall | 0.888889 |
| F1 score | 0.842105 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
