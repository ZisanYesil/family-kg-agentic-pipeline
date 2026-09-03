# Triple matching report: 570

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Hot_Time_in_the_Town_of_Berlin | hasComposer | Joe_Bushkin |
| Joe_Bushkin | hasDeathPlace | Santa_Barbara |

# 2. Unmatched triples

**Total unmatched count: 10**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 10**

| Subject | Predicate | Object |
|---|---|---|
| Hot_Time_in_the_Town_of_Berlin | type | MusicalWork |
| Hot_Time_in_the_Town_of_Berlin | type | NamedIndividual |
| Hot_Time_in_the_Town_of_Berlin | label | "(There'll Be a) Hot Time in the Town of Berlin" |
| Joe_Bushkin | type | Person |
| Joe_Bushkin | type | NamedIndividual |
| Joe_Bushkin | label | "Joe Bushkin" |
| Joe_Bushkin | altLabel | "Bushkin" |
| Santa_Barbara | type | Place |
| Santa_Barbara | type | NamedIndividual |
| Santa_Barbara | label | "Santa Barbara, California" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 12 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 10 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.166667 |
| Recall | 1.000000 |
| F1 score | 0.285714 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
