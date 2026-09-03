# Triple matching report: 17

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Charles_Willoughby_10th_Baron_Willoughby_of_Parham | hasParent | William_Willoughby |
| William_Willoughby | hasParent | Lady_Frances_Manners |

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
| Charles_Willoughby_10th_Baron_Willoughby_of_Parham | type | Person |
| Charles_Willoughby_10th_Baron_Willoughby_of_Parham | type | NamedIndividual |
| Charles_Willoughby_10th_Baron_Willoughby_of_Parham | label | "Charles Willoughby, 10th Baron Willoughby of Parham" |
| Lady_Frances_Manners | type | Person |
| Lady_Frances_Manners | type | NamedIndividual |
| Lady_Frances_Manners | label | "Frances Manners" |
| William_Willoughby | type | Person |
| William_Willoughby | type | NamedIndividual |
| William_Willoughby | label | "William Willoughby, 6th Baron Willoughby of Parham" |

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
