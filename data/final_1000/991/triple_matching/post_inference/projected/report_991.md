# Triple matching report: 991

# 1. Matched triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| George_Clooney | hasCountry | American |
| George_Clooney | type | Agent |
| George_Clooney | type | Person |
| Killer_s_Romance | hasCreator | Phillip_Ko |
| Killer_s_Romance | hasDirector | Phillip_Ko |
| Killer_s_Romance | type | Artifact |
| Killer_s_Romance | type | CreativeWork |
| Killer_s_Romance | type | Film |
| Phillip_Ko | type | Agent |
| Phillip_Ko | type | Person |
| The_Ides_of_March_2011_film | hasCreator | George_Clooney |
| The_Ides_of_March_2011_film | hasDirector | George_Clooney |
| The_Ides_of_March_2011_film | type | Artifact |
| The_Ides_of_March_2011_film | type | CreativeWork |
| The_Ides_of_March_2011_film | type | Film |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| China | type | Country |
| China | type | Place |
| Phillip_Ko | hasCountry | China |

## 2.2 Extracted-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Phillip_Ko | hasCountry | country_hongkong |
| country_hongkong | type | Country |
| country_hongkong | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 20 |
| Union triples in scope | 23 |
| True positives (matched) | 17 |
| False positives (extracted-only) | 3 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.850000 |
| Recall | 0.850000 |
| F1 score | 0.850000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
