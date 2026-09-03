# Triple matching report: 677

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Matilda_of_Carinthia | hasParent | Uta_of_Passau |
| Theobald_II_Count_of_Champagne | hasSpouse | Matilda_of_Carinthia |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Matilda_of_Carinthia | type | Person |
| Matilda_of_Carinthia | type | NamedIndividual |
| Matilda_of_Carinthia | label | "Matilda of Carinthia" |
| Matilda_of_Carinthia | altLabel | "Mathilde of Sponheim" |
| Theobald_II_Count_of_Champagne | type | Person |
| Theobald_II_Count_of_Champagne | type | NamedIndividual |
| Theobald_II_Count_of_Champagne | label | "Theobald II, Count of Champagne" |
| Theobald_II_Count_of_Champagne | altLabel | "Theobald the Great" |
| Theobald_II_Count_of_Champagne | altLabel | "Thibaut de Blois" |
| Uta_of_Passau | type | Person |
| Uta_of_Passau | type | NamedIndividual |
| Uta_of_Passau | label | "Uta of Passau" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 14 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.142857 |
| Recall | 1.000000 |
| F1 score | 0.250000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
