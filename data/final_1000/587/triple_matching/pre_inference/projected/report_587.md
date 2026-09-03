# Triple matching report: 587

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Basu_Bhattacharya | hasChild | Aditya_Bhattacharya |
| Griha_Pravesh | hasDirector | Basu_Bhattacharya |

# 2. Unmatched triples

**Total unmatched count: 17**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 17**

| Subject | Predicate | Object |
|---|---|---|
| Aditya_Bhattacharya | type | Person |
| Aditya_Bhattacharya | type | NamedIndividual |
| Aditya_Bhattacharya | label | "Aditya Bhattacharya" |
| Basu_Bhattacharya | hasChild | anwesha_arya |
| Basu_Bhattacharya | hasChild | chimmu |
| Basu_Bhattacharya | type | Person |
| Basu_Bhattacharya | type | NamedIndividual |
| Basu_Bhattacharya | label | "Basu Bhattacharya" |
| Griha_Pravesh | type | Film |
| Griha_Pravesh | type | NamedIndividual |
| Griha_Pravesh | label | "Griha Pravesh" |
| anwesha_arya | type | Person |
| anwesha_arya | type | NamedIndividual |
| anwesha_arya | label | "Anwesha Arya" |
| chimmu | type | Person |
| chimmu | type | NamedIndividual |
| chimmu | label | "Chimmu" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 19 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 19 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 17 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.105263 |
| Recall | 1.000000 |
| F1 score | 0.190476 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
