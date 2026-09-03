# Triple matching report: 114

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Adolf_VII_of_Berg | hasDeathPlace | Neuss |
| Henry_of_Berg_Lord_of_Windeck | hasParent | Adolf_VII_of_Berg |

# 2. Unmatched triples

**Total unmatched count: 9**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 9**

| Subject | Predicate | Object |
|---|---|---|
| Adolf_VII_of_Berg | type | Person |
| Adolf_VII_of_Berg | type | NamedIndividual |
| Adolf_VII_of_Berg | label | "Adolf VII of Berg" |
| Henry_of_Berg_Lord_of_Windeck | type | Person |
| Henry_of_Berg_Lord_of_Windeck | type | NamedIndividual |
| Henry_of_Berg_Lord_of_Windeck | label | "Henry of Berg, Lord of Windeck" |
| Neuss | type | Place |
| Neuss | type | NamedIndividual |
| Neuss | label | "Neuss" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 11 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 11 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 9 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.181818 |
| Recall | 1.000000 |
| F1 score | 0.307692 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
