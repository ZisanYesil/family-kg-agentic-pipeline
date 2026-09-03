# Triple matching report: 831

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| A_Heart_Returns_Home | hasCountry | German |
| The_Manny | hasCountry | German |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| A_Heart_Returns_Home | type | Film |
| A_Heart_Returns_Home | type | NamedIndividual |
| A_Heart_Returns_Home | label | "A Heart Returns Home" |
| German | type | Country |
| German | type | NamedIndividual |
| German | label | "Germany" |
| German | altLabel | "German" |
| German | altLabel | "West German" |
| The_Manny | type | Film |
| The_Manny | type | NamedIndividual |
| The_Manny | label | "The Manny" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.153846 |
| Recall | 1.000000 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
