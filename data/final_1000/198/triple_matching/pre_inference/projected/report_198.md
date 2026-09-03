# Triple matching report: 198

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Alibi_Bye_Bye | hasDirector | Ben_Holmes |
| Ben_Holmes | hasCountry | American |
| Leave_It_to_the_Marines | hasDirector | Sam_Newfield |
| Sam_Newfield | hasCountry | American |

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
| Alibi_Bye_Bye | type | Film |
| Alibi_Bye_Bye | type | NamedIndividual |
| Alibi_Bye_Bye | label | "Alibi Bye Bye" |
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Ben_Holmes | type | Person |
| Ben_Holmes | type | NamedIndividual |
| Ben_Holmes | label | "Ben Holmes" |
| Leave_It_to_the_Marines | type | Film |
| Leave_It_to_the_Marines | type | NamedIndividual |
| Leave_It_to_the_Marines | label | "Leave It To The Marines" |
| Sam_Newfield | type | Person |
| Sam_Newfield | type | NamedIndividual |
| Sam_Newfield | label | "Sam Newfield" |

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
