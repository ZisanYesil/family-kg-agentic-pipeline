# Triple matching report: 823

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Do_You_Like_This | hasPerformer | Rome |
| Rome | hasBirthPlace | Benton_Harbor_Michigan |

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
| Benton_Harbor_Michigan | type | Place |
| Benton_Harbor_Michigan | type | NamedIndividual |
| Benton_Harbor_Michigan | label | "Benton Harbor, Michigan" |
| Do_You_Like_This | type | MusicalWork |
| Do_You_Like_This | type | NamedIndividual |
| Do_You_Like_This | label | "Do You Like This" |
| Rome | type | Person |
| Rome | type | NamedIndividual |
| Rome | label | "Rome" |
| Rome | altLabel | "Jerome Woods" |

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
