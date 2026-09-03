# Triple matching report: 129

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| I_Believe_in_Your_Sweet_Love | hasPerformer | Bonnie_Tyler |

# 2. Unmatched triples

**Total unmatched count: 12**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Bonnie_Tyler | hasCountry | United_Kingdom |

## 2.2 Extracted-only triples

**Count: 11**

| Subject | Predicate | Object |
|---|---|---|
| Bonnie_Tyler | hasCountry | wales |
| Bonnie_Tyler | type | Person |
| Bonnie_Tyler | type | NamedIndividual |
| Bonnie_Tyler | label | "Bonnie Tyler" |
| I_Believe_in_Your_Sweet_Love | type | CreativeWork |
| I_Believe_in_Your_Sweet_Love | type | NamedIndividual |
| I_Believe_in_Your_Sweet_Love | label | "I Believe in Your Sweet Love" |
| wales | type | Country |
| wales | type | NamedIndividual |
| wales | label | "Wales" |
| wales | altLabel | "Welsh" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 12 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 13 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 11 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.083333 |
| Recall | 0.500000 |
| F1 score | 0.142857 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
