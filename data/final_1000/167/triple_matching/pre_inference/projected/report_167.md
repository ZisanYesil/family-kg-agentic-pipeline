# Triple matching report: 167

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Black_Gravel | hasDirector | Helmut_Käutner |
| Helmut_Käutner | hasCountry | Germany |
| The_Little_Napoleon | hasDirector | Georg_Jacoby |

# 2. Unmatched triples

**Total unmatched count: 18**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Georg_Jacoby | hasCountry | German |

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| Black_Gravel | type | Film |
| Black_Gravel | type | NamedIndividual |
| Black_Gravel | label | "Black Gravel" |
| Georg_Jacoby | hasCountry | Germany |
| Georg_Jacoby | type | Person |
| Georg_Jacoby | type | NamedIndividual |
| Georg_Jacoby | label | "Georg Jacoby" |
| Germany | type | Country |
| Germany | type | NamedIndividual |
| Germany | label | "Germany" |
| Germany | altLabel | "German" |
| Helmut_Käutner | type | Person |
| Helmut_Käutner | type | NamedIndividual |
| Helmut_Käutner | label | "Helmut Käutner" |
| The_Little_Napoleon | type | Film |
| The_Little_Napoleon | type | NamedIndividual |
| The_Little_Napoleon | label | "The Little Napoleon" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 21 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.150000 |
| Recall | 0.750000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
