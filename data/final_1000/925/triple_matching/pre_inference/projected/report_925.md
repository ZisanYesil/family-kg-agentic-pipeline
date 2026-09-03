# Triple matching report: 925

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Donatus_Prince_and_Landgrave_of_Hesse | hasParent | Moritz_Landgrave_of_Hesse |
| Moritz_Landgrave_of_Hesse | hasBirthDate | "1926-08-06"^^<http://www.w3.org/2001/XMLSchema#date> |

# 2. Unmatched triples

**Total unmatched count: 6**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Donatus_Prince_and_Landgrave_of_Hesse | type | Person |
| Donatus_Prince_and_Landgrave_of_Hesse | type | NamedIndividual |
| Donatus_Prince_and_Landgrave_of_Hesse | label | "Donatus, Landgrave of Hesse" |
| Moritz_Landgrave_of_Hesse | type | Person |
| Moritz_Landgrave_of_Hesse | type | NamedIndividual |
| Moritz_Landgrave_of_Hesse | label | "Moritz, Landgrave of Hesse" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 8 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 8 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 6 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.250000 |
| Recall | 1.000000 |
| F1 score | 0.400000 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
