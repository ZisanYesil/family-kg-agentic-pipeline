# Triple matching report: 932

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Hubert_Humphrey | hasBirthPlace | Wallace |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Hubert_Horatio_Skip_Humphrey | hasParent | Hubert_Humphrey |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Hubert_Horatio_Skip_Humphrey | type | Person |
| Hubert_Horatio_Skip_Humphrey | type | NamedIndividual |
| Hubert_Horatio_Skip_Humphrey | label | "Hubert Horatio \"Skip\" Humphrey III" |
| Hubert_Horatio_Skip_Humphrey | altLabel | "Skip Humphrey" |
| Hubert_Humphrey | hasChild | Hubert_Horatio_Skip_Humphrey |
| Hubert_Humphrey | type | Person |
| Hubert_Humphrey | type | NamedIndividual |
| Hubert_Humphrey | label | "Hubert Horatio Humphrey Jr." |
| Hubert_Humphrey | altLabel | "Hubert Humphrey" |
| Wallace | type | Place |
| Wallace | type | NamedIndividual |
| Wallace | label | "Wallace, South Dakota" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
