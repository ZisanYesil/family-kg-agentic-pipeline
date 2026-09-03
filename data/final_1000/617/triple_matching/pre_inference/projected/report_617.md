# Triple matching report: 617

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Fred_Fisher | hasCountry | American |
| Oui_Oui_Marie | hasComposer | Fred_Fisher |

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
| Fred_Fisher | type | Person |
| Fred_Fisher | type | NamedIndividual |
| Fred_Fisher | label | "Fred Fisher" |
| Fred_Fisher | altLabel | "Alfred Breitenbach" |
| Oui_Oui_Marie | type | MusicalWork |
| Oui_Oui_Marie | type | NamedIndividual |
| Oui_Oui_Marie | label | "Oui, Oui, Marie" |

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
