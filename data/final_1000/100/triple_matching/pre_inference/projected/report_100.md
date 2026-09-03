# Triple matching report: 100

# 1. Matched triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Cursed_2005_film | hasDirector | Wes_Craven |
| Ralph_Nelson | hasCountry | American |
| The_Wrath_of_God | hasDirector | Ralph_Nelson |
| Wes_Craven | hasCountry | American |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Cursed_2005_film | type | Film |
| Cursed_2005_film | type | NamedIndividual |
| Cursed_2005_film | label | "Cursed (2005 film)" |
| Ralph_Nelson | type | Person |
| Ralph_Nelson | type | NamedIndividual |
| Ralph_Nelson | label | "Ralph Nelson" |
| The_Wrath_of_God | type | Film |
| The_Wrath_of_God | type | NamedIndividual |
| The_Wrath_of_God | label | "The Wrath of God" |
| Wes_Craven | type | Person |
| Wes_Craven | type | NamedIndividual |
| Wes_Craven | label | "Wes Craven" |
| Wes_Craven | altLabel | "Wesley Earl Craven" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 21 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 21 |
| True positives (matched) | 4 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.190476 |
| Recall | 1.000000 |
| F1 score | 0.320000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
