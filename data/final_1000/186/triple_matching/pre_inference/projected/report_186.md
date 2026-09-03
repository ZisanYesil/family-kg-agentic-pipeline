# Triple matching report: 186

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| His_Name_Was_Holy_Ghost | hasCountry | Italian |
| The_Cop_in_Blue_Jeans | hasCountry | Italian |

# 2. Unmatched triples

**Total unmatched count: 11**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| His_Name_Was_Holy_Ghost | hasCountry | Spanish |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| His_Name_Was_Holy_Ghost | type | Film |
| His_Name_Was_Holy_Ghost | type | NamedIndividual |
| His_Name_Was_Holy_Ghost | label | "His Name Was Holy Ghost" |
| Italian | type | Country |
| Italian | type | NamedIndividual |
| Italian | label | "Italy" |
| Italian | altLabel | "Italian" |
| The_Cop_in_Blue_Jeans | type | Film |
| The_Cop_in_Blue_Jeans | type | NamedIndividual |
| The_Cop_in_Blue_Jeans | label | "The Cop In Blue Jeans" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 3 |
| Union triples in scope | 13 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.166667 |
| Recall | 0.666667 |
| F1 score | 0.266667 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
