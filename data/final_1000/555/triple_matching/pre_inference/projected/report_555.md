# Triple matching report: 555

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Blake_Edwards | hasCountry | American |
| Operation_Petticoat | hasDirector | Blake_Edwards |
| War_Book | hasDirector | Tom_Harper |

# 2. Unmatched triples

**Total unmatched count: 22**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Tom_Harper_director | hasCountry | British |

## 2.2 Extracted-only triples

**Count: 21**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Blake_Edwards | type | Person |
| Blake_Edwards | type | NamedIndividual |
| Blake_Edwards | label | "Blake Edwards" |
| British | type | Country |
| British | type | NamedIndividual |
| British | label | "United Kingdom" |
| British | altLabel | "British" |
| Operation_Petticoat | type | Film |
| Operation_Petticoat | type | NamedIndividual |
| Operation_Petticoat | label | "Operation Petticoat" |
| Tom_Harper | hasCountry | British |
| Tom_Harper | type | Person |
| Tom_Harper | type | NamedIndividual |
| Tom_Harper | label | "Tom Harper" |
| War_Book | type | Film |
| War_Book | type | NamedIndividual |
| War_Book | label | "War Book" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 6 |
| Extracted triples in scope | 24 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 25 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 21 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.125000 |
| Recall | 0.750000 |
| F1 score | 0.214286 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
