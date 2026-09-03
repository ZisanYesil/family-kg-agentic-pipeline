# Triple matching report: 807

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Lil_Boosie | hasBirthPlace | Baton_Rouge |
| Show_da_World | hasPerformer | Lil_Boosie |

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
| Baton_Rouge | type | Place |
| Baton_Rouge | type | NamedIndividual |
| Baton_Rouge | label | "Baton Rouge, Louisiana" |
| Lil_Boosie | type | Person |
| Lil_Boosie | type | NamedIndividual |
| Lil_Boosie | label | "Boosie Badazz" |
| Lil_Boosie | altLabel | "Lil Boosie" |
| Lil_Boosie | altLabel | "Torrence Hatch Jr." |
| Show_da_World | type | MusicalWork |
| Show_da_World | type | NamedIndividual |
| Show_da_World | label | "Show da World" |

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
