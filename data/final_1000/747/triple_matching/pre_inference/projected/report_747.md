# Triple matching report: 747

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Godfrey_IV_Duke_of_Lower_Lorraine | hasSpouse | Matilda_of_Tuscany |
| Ida_of_Lorraine | hasSibling | Godfrey_IV_Duke_of_Lower_Lorraine |

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
| Godfrey_IV_Duke_of_Lower_Lorraine | type | Person |
| Godfrey_IV_Duke_of_Lower_Lorraine | type | NamedIndividual |
| Godfrey_IV_Duke_of_Lower_Lorraine | label | "Godfrey IV, Duke of Lower Lorraine" |
| Ida_of_Lorraine | type | Person |
| Ida_of_Lorraine | type | NamedIndividual |
| Ida_of_Lorraine | label | "Ida of Lorraine" |
| Matilda_of_Tuscany | type | Person |
| Matilda_of_Tuscany | type | NamedIndividual |
| Matilda_of_Tuscany | label | "Matilda of Tuscany" |

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
