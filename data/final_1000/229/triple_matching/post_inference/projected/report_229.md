# Triple matching report: 229

# 1. Matched triples

**Count: 19**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| British | type | Country |
| British | type | Place |
| David_Butler | type | Agent |
| David_Butler | type | Person |
| It_s_a_Great_Feeling | hasCreator | David_Butler |
| It_s_a_Great_Feeling | hasDirector | David_Butler |
| It_s_a_Great_Feeling | type | Artifact |
| It_s_a_Great_Feeling | type | CreativeWork |
| It_s_a_Great_Feeling | type | Film |
| Oklahoma_1999_film | hasCreator | Trevor_Nunn |
| Oklahoma_1999_film | hasDirector | Trevor_Nunn |
| Oklahoma_1999_film | type | Artifact |
| Oklahoma_1999_film | type | CreativeWork |
| Oklahoma_1999_film | type | Film |
| Trevor_Nunn | hasCountry | British |
| Trevor_Nunn | type | Agent |
| Trevor_Nunn | type | Person |

# 2. Unmatched triples

**Total unmatched count: 4**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| David_Butler_director | hasCountry | American |
| David_Butler_director | type | Agent |
| David_Butler_director | type | Person |

## 2.2 Extracted-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| David_Butler | hasCountry | American |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 6 |
| Extracted triples in scope | 20 |
| Ground-truth triples in scope | 22 |
| Union triples in scope | 23 |
| True positives (matched) | 19 |
| False positives (extracted-only) | 1 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.950000 |
| Recall | 0.863636 |
| F1 score | 0.904762 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
