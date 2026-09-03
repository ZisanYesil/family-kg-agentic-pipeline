# Triple matching report: 20

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Jim_Jarmusch | hasCountry | American |
| Winter_Meeting | hasDirector | Bretaigne_Windust |
| Year_of_the_Horse | hasDirector | Jim_Jarmusch |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Bretaigne_Windust | hasCountry | French |

## 2.2 Extracted-only triples

**Count: 16**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | NamedIndividual |
| American | label | "United States" |
| American | altLabel | "American" |
| Bretaigne_Windust | type | Person |
| Bretaigne_Windust | type | NamedIndividual |
| Bretaigne_Windust | label | "Bretaigne Windust" |
| Jim_Jarmusch | type | Person |
| Jim_Jarmusch | type | NamedIndividual |
| Jim_Jarmusch | label | "Jim Jarmusch" |
| Winter_Meeting | type | Film |
| Winter_Meeting | type | NamedIndividual |
| Winter_Meeting | label | "Winter Meeting" |
| Year_of_the_Horse | type | Film |
| Year_of_the_Horse | type | NamedIndividual |
| Year_of_the_Horse | label | "Year of the Horse" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 20 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 16 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.157895 |
| Recall | 0.750000 |
| F1 score | 0.260870 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
