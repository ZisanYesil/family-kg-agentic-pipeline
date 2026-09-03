# Triple matching report: 991

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| George_Clooney | hasCountry | American |
| Killer_s_Romance | hasDirector | Phillip_Ko |
| The_Ides_of_March_2011_film | hasDirector | George_Clooney |

# 2. Unmatched triples

**Total unmatched count: 21**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Phillip_Ko | hasCountry | China |

## 2.2 Extracted-only triples

**Count: 20**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| George_Clooney | type | Person |
| George_Clooney | type | NamedIndividual |
| George_Clooney | label | "George Clooney" |
| Killer_s_Romance | type | Film |
| Killer_s_Romance | type | NamedIndividual |
| Killer_s_Romance | label | "Killer's Romance" |
| Phillip_Ko | hasCountry | country_hongkong |
| Phillip_Ko | type | Person |
| Phillip_Ko | type | NamedIndividual |
| Phillip_Ko | label | "Phillip Ko" |
| The_Ides_of_March_2011_film | type | Film |
| The_Ides_of_March_2011_film | type | NamedIndividual |
| The_Ides_of_March_2011_film | label | "The Ides of March (2011 film)" |
| country_hongkong | type | Country |
| country_hongkong | type | NamedIndividual |
| country_hongkong | label | "Hong Kong" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 23 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 24 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 20 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.130435 |
| Recall | 0.750000 |
| F1 score | 0.222222 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
