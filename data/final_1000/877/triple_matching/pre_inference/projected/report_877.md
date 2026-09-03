# Triple matching report: 877

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Article_99 | hasCountry | American |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Six_Dance_Lessons_in_Six_Weeks_film | hasCountry | Hungarian |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Article_99 | type | Film |
| Article_99 | type | NamedIndividual |
| Article_99 | label | "Article 99" |
| Six_Dance_Lessons_in_Six_Weeks_film | hasCountry | American |
| Six_Dance_Lessons_in_Six_Weeks_film | type | Film |
| Six_Dance_Lessons_in_Six_Weeks_film | type | NamedIndividual |
| Six_Dance_Lessons_in_Six_Weeks_film | label | "Six Dance Lessons in Six Weeks" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
