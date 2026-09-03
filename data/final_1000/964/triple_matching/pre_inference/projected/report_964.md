# Triple matching report: 964

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Louis_Jean_Marie_de_Bourbon | hasCountry | France |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Louis_Alexandre_Prince_of_Lamballe | hasParent | Louis_Jean_Marie_de_Bourbon |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| France | type | Country |
| France | type | NamedIndividual |
| France | label | "France" |
| France | altLabel | "French" |
| Louis_Alexandre_Prince_of_Lamballe | type | Person |
| Louis_Alexandre_Prince_of_Lamballe | type | NamedIndividual |
| Louis_Alexandre_Prince_of_Lamballe | label | "Louis Alexandre de Bourbon" |
| Louis_Jean_Marie_de_Bourbon | hasChild | Louis_Alexandre_Prince_of_Lamballe |
| Louis_Jean_Marie_de_Bourbon | type | Person |
| Louis_Jean_Marie_de_Bourbon | type | NamedIndividual |
| Louis_Jean_Marie_de_Bourbon | label | "Louis Jean Marie de Bourbon" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
