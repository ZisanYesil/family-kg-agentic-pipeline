# Triple matching report: 516

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| The_To_Do_List | hasCountry | American |
| The_Twelve_Chairs_1970_film | hasCountry | American |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| The_To_Do_List | type | Film |
| The_To_Do_List | type | NamedIndividual |
| The_To_Do_List | label | "The To Do List" |
| The_Twelve_Chairs_1970_film | type | Film |
| The_Twelve_Chairs_1970_film | type | NamedIndividual |
| The_Twelve_Chairs_1970_film | label | "The Twelve Chairs (1970 film)" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
