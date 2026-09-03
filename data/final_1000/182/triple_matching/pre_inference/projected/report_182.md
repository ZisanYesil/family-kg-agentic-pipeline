# Triple matching report: 182

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| A_Heart_in_Winter | hasDirector | Claude_Sautet |
| Barbet_Schroeder | hasCountry | Swiss |
| Claude_Sautet | hasCountry | French |
| Single_White_Female | hasDirector | Barbet_Schroeder |

# 2. Unmatched triples

**Total unmatched count: 21**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Barbet_Schroeder | hasCountry | French |

## 2.2 Extracted-only triples

**Count: 20**

| Subject | Predicate | Object |
|---|---|---|
| A_Heart_in_Winter | type | Film |
| A_Heart_in_Winter | type | NamedIndividual |
| A_Heart_in_Winter | label | "A Heart In Winter" |
| Barbet_Schroeder | type | Person |
| Barbet_Schroeder | type | NamedIndividual |
| Barbet_Schroeder | label | "Barbet Schroeder" |
| Claude_Sautet | type | Person |
| Claude_Sautet | type | NamedIndividual |
| Claude_Sautet | label | "Claude Sautet" |
| French | type | Country |
| French | type | NamedIndividual |
| French | label | "France" |
| French | altLabel | "French" |
| Single_White_Female | type | Film |
| Single_White_Female | type | NamedIndividual |
| Single_White_Female | label | "Single White Female" |
| Swiss | type | Country |
| Swiss | type | NamedIndividual |
| Swiss | label | "Switzerland" |
| Swiss | altLabel | "Swiss" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 6 |
| Extracted triples in scope | 24 |
| Ground-truth triples in scope | 5 |
| Union triples in scope | 25 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 20 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.166667 |
| Recall | 0.800000 |
| F1 score | 0.275862 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
