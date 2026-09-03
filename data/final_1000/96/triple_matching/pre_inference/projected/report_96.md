# Triple matching report: 96

# 1. Matched triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Anne_Castles | hasOccupation | cognitive_scientist |
| Colin_Will | hasOccupation | poet |
| Colin_Will | hasOccupation | publisher |

# 2. Unmatched triples

**Total unmatched count: 16**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Colin_Will | hasOccupation | librarian |

## 2.2 Extracted-only triples

**Count: 15**

| Subject | Predicate | Object |
|---|---|---|
| Anne_Castles | type | Person |
| Anne_Castles | type | NamedIndividual |
| Anne_Castles | label | "Anne Castles" |
| Colin_Will | type | Person |
| Colin_Will | type | NamedIndividual |
| Colin_Will | label | "Colin Will" |
| cognitive_scientist | type | Occupation |
| cognitive_scientist | type | NamedIndividual |
| cognitive_scientist | label | "cognitive scientist" |
| poet | type | Occupation |
| poet | type | NamedIndividual |
| poet | label | "poet" |
| publisher | type | Occupation |
| publisher | type | NamedIndividual |
| publisher | label | "publisher" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 5 |
| Extracted triples in scope | 18 |
| Ground-truth triples in scope | 4 |
| Union triples in scope | 19 |
| True positives (matched) | 3 |
| False positives (extracted-only) | 15 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.166667 |
| Recall | 0.750000 |
| F1 score | 0.272727 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
