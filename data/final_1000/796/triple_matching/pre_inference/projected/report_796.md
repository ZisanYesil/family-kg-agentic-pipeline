# Triple matching report: 796

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Dark_Is_the_Night | hasComposer | Nikita_Bogoslovsky |
| Nikita_Bogoslovsky | hasBirthPlace | Petersburg |

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
| Dark_Is_the_Night | type | MusicalWork |
| Dark_Is_the_Night | type | NamedIndividual |
| Dark_Is_the_Night | label | "Dark Is The Night (Soviet song)" |
| Nikita_Bogoslovsky | type | Person |
| Nikita_Bogoslovsky | type | NamedIndividual |
| Nikita_Bogoslovsky | label | "Nikita Bogoslovsky" |
| Petersburg | type | Place |
| Petersburg | type | NamedIndividual |
| Petersburg | label | "Saint-Petersburg" |

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
