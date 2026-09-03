# Triple matching report: 302

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Anne_Marie_Thérèse_of_Lorraine | hasParent | Claude_Françoise_de_Lorraine |
| Claude_Françoise_de_Lorraine | hasSibling | Nicole_Duchess_of_Lorraine |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Anne_Marie_Thérèse_of_Lorraine | type | Person |
| Anne_Marie_Thérèse_of_Lorraine | type | NamedIndividual |
| Anne_Marie_Thérèse_of_Lorraine | label | "Anne Marie Thérèse de Lorraine" |
| Claude_Françoise_de_Lorraine | type | Person |
| Claude_Françoise_de_Lorraine | type | NamedIndividual |
| Claude_Françoise_de_Lorraine | label | "Claude Françoise de Lorraine" |
| Nicole_Duchess_of_Lorraine | type | Person |
| Nicole_Duchess_of_Lorraine | type | NamedIndividual |
| Nicole_Duchess_of_Lorraine | label | "Nicole, Duchess of Lorraine" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
