# Triple matching report: 20

# 1. Matched triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| American | type | Country |
| American | type | Place |
| Bretaigne_Windust | type | Agent |
| Bretaigne_Windust | type | Person |
| Jim_Jarmusch | hasCountry | American |
| Jim_Jarmusch | type | Agent |
| Jim_Jarmusch | type | Person |
| Winter_Meeting | hasCreator | Bretaigne_Windust |
| Winter_Meeting | hasDirector | Bretaigne_Windust |
| Winter_Meeting | type | Artifact |
| Winter_Meeting | type | CreativeWork |
| Winter_Meeting | type | Film |
| Year_of_the_Horse | hasCreator | Jim_Jarmusch |
| Year_of_the_Horse | hasDirector | Jim_Jarmusch |
| Year_of_the_Horse | type | Artifact |
| Year_of_the_Horse | type | CreativeWork |
| Year_of_the_Horse | type | Film |

# 2. Unmatched triples

**Total unmatched count: 3**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Bretaigne_Windust | hasCountry | French |
| French | type | Country |
| French | type | Place |

## 2.2 Extracted-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 17 |
| Ground-truth triples in scope | 20 |
| Union triples in scope | 20 |
| True positives (matched) | 17 |
| False positives (extracted-only) | 0 |
| False negatives (ground-truth-only) | 3 |
| Precision | 1.000000 |
| Recall | 0.850000 |
| F1 score | 0.918919 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
