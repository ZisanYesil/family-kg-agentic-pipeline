# Triple matching report: 323

# 1. Matched triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| George_Charles_Wallich | hasParent | Nathaniel_Wallich |
| Nathaniel_Wallich | hasEmployer | Calcutta_Botanical_Garden |

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| George_Charles_Wallich | type | Person |
| George_Charles_Wallich | type | NamedIndividual |
| George_Charles_Wallich | label | "George Charles Wallich" |
| Nathaniel_Wallich | hasParent | George_Charles_Wallich |
| Nathaniel_Wallich | type | Person |
| Nathaniel_Wallich | type | NamedIndividual |
| Nathaniel_Wallich | label | "Nathaniel Wallich" |
| royal_botanical_gardens | type | Place |
| royal_botanical_gardens | type | NamedIndividual |
| royal_botanical_gardens | label | "Royal Botanical Gardens" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 0 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 2 |
| Precision | 0.000000 |
| Recall | 0.000000 |
| F1 score | 0.000000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
