# Triple matching report: 814

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Bernadine | hasPerformer | Pat_Boone |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Pat_Boone | hasAwardReceived | Gospel_Music_Hall_of_Fame |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Bernadine | type | MusicalWork |
| Bernadine | type | NamedIndividual |
| Bernadine | label | "Bernardine" |
| Bernadine | altLabel | "Bernardine" |
| Gospel_Music_Hall_of_Fame | type | Award |
| Gospel_Music_Hall_of_Fame | type | NamedIndividual |
| Gospel_Music_Hall_of_Fame | label | "Gospel Music Hall of Fame" |
| Gospel_Music_Hall_of_Fame | altLabel | "Gospel Music Hall of Fame" |
| Pat_Boone | type | Person |
| Pat_Boone | type | NamedIndividual |
| Pat_Boone | label | "Pat Boone" |
| Pat_Boone | altLabel | "Pat Boone" |

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
