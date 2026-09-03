# Triple matching report: 882

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| John_Roberts | hasCountry | American |
| War_of_the_Buttons | hasDirector | John_Roberts |

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
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| John_Roberts | type | Person |
| John_Roberts | type | NamedIndividual |
| John_Roberts | label | "John Roberts" |
| John_Roberts | altLabel | "John Glover Roberts Jr." |
| War_of_the_Buttons | type | Film |
| War_of_the_Buttons | type | NamedIndividual |
| War_of_the_Buttons | label | "War of the Buttons (1994 film)" |

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
