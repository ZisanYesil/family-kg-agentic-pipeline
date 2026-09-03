# Triple matching report: 445

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Marvin_Hatley | hasDeathPlace | Hollywood_California |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| There_Goes_My_Heart | hasComposer | Marvin_Hatley |

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Hollywood_California | type | Place |
| Hollywood_California | type | NamedIndividual |
| Hollywood_California | label | "Hollywood, California" |
| Marvin_Hatley | type | Person |
| Marvin_Hatley | type | NamedIndividual |
| Marvin_Hatley | label | "Marvin Hatley" |
| There_Goes_My_Heart | type | Film |
| There_Goes_My_Heart | type | NamedIndividual |
| There_Goes_My_Heart | label | "There Goes My Heart" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.100000 |
| Recall | 0.500000 |
| F1 score | 0.166667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
