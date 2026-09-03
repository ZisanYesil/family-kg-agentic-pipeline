# Triple matching report: 505

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| An_Ideal_Woman | hasDirector | Jean_Durand |
| François_Leterrier | hasCountry | French |
| Goodbye_Emmanuelle | hasDirector | François_Leterrier |
| Jean_Durand | hasCountry | French |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| An_Ideal_Woman | type | Film |
| An_Ideal_Woman | type | NamedIndividual |
| An_Ideal_Woman | label | "An Ideal Woman" |
| François_Leterrier | type | Person |
| François_Leterrier | type | NamedIndividual |
| François_Leterrier | label | "François Leterrier" |
| French | type | Country |
| French | type | NamedIndividual |
| French | label | "France" |
| French | altLabel | "French" |
| Goodbye_Emmanuelle | type | Film |
| Goodbye_Emmanuelle | type | NamedIndividual |
| Goodbye_Emmanuelle | label | "Goodbye Emmanuelle" |
| Jean_Durand | type | Person |
| Jean_Durand | type | NamedIndividual |
| Jean_Durand | label | "Jean Durand" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 20 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.200000 |
| Recall | 1.000000 |
| F1 score | 0.333333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
