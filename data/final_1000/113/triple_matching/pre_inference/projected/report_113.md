# Triple matching report: 113

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| A_Rough_Passage | hasDirector | Franklyn_Barrett |
| Franklyn_Barrett | hasCountry | Australian |
| The_Green_God_film | hasDirector | Paul_Scardon |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Paul_Scardon | hasCountry | Australian |

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| A_Rough_Passage | type | Film |
| A_Rough_Passage | type | NamedIndividual |
| A_Rough_Passage | label | "A Rough Passage" |
| Australian | type | Country |
| Australian | type | NamedIndividual |
| Australian | label | "Australia" |
| Australian | altLabel | "Australian" |
| Franklyn_Barrett | type | Person |
| Franklyn_Barrett | type | NamedIndividual |
| Franklyn_Barrett | label | "Franklyn Barrett" |
| Paul_Scardon | type | Person |
| Paul_Scardon | type | NamedIndividual |
| Paul_Scardon | label | "Paul Scardon" |
| The_Green_God_film | type | Film |
| The_Green_God_film | type | NamedIndividual |
| The_Green_God_film | label | "The Green God" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 20 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.157895 |
| Recall | 0.750000 |
| F1 score | 0.260870 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
