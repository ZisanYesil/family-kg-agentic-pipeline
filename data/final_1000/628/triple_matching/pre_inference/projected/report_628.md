# Triple matching report: 628

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Pugachev | hasDirector | Aleksei_Saltykov |

# 2. Unmatched triples

**Total unmatched count: 14**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Aleksey_Aleksandrovich_Saltykov | hasAwardReceived | People_s_Artist_of_the_RSFSR |

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Aleksei_Saltykov | hasAwardReceived | People_s_Artist_of_the_RSFSR |
| Aleksei_Saltykov | type | Person |
| Aleksei_Saltykov | type | NamedIndividual |
| Aleksei_Saltykov | label | "Aleksei Saltykov" |
| Aleksei_Saltykov | altLabel | "Aleksey Aleksandrovich Saltykov" |
| Aleksei_Saltykov | altLabel | "Alexey Saltykov" |
| People_s_Artist_of_the_RSFSR | type | Award |
| People_s_Artist_of_the_RSFSR | type | NamedIndividual |
| People_s_Artist_of_the_RSFSR | label | "People's Artist of the RSFSR" |
| Pugachev | hasPublicationDate | "1978"^^<http://www.w3.org/2001/XMLSchema#gYear> |
| Pugachev | type | Film |
| Pugachev | type | NamedIndividual |
| Pugachev | label | "Pugachev" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.071429 |
| Recall | 0.500000 |
| F1 score | 0.125000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
