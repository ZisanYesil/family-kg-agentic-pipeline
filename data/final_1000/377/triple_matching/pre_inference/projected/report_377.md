# Triple matching report: 377

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| John_II_of_Namur | hasParent | John_I_Marquis_of_Namur |
| John_I_Marquis_of_Namur | hasParent | Isabelle_of_Luxembourg |

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
| Isabelle_of_Luxembourg | type | Person |
| Isabelle_of_Luxembourg | type | NamedIndividual |
| Isabelle_of_Luxembourg | label | "Isabelle of Luxembourg" |
| John_II_of_Namur | type | Person |
| John_II_of_Namur | type | NamedIndividual |
| John_II_of_Namur | label | "John II, Marquis of Namur" |
| John_I_Marquis_of_Namur | type | Person |
| John_I_Marquis_of_Namur | type | NamedIndividual |
| John_I_Marquis_of_Namur | label | "John I, Marquis of Namur" |

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
