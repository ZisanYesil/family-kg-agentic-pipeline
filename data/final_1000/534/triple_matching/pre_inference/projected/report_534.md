# Triple matching report: 534

# 1. Matched triples

**Count: 5**

| Subject | Predicate | Object |
|---|---|---|
| Amir_Hossein_Arman | hasOccupation | actor |
| Amir_Hossein_Arman | hasOccupation | model |
| Amir_Hossein_Arman | hasOccupation | singer |
| Inbakavi | hasOccupation | dramatist |
| Inbakavi | hasOccupation | poet |

# 2. Unmatched triples

**Total unmatched count: 22**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 22**

| Subject | Predicate | Object |
|---|---|---|
| Amir_Hossein_Arman | type | Person |
| Amir_Hossein_Arman | type | NamedIndividual |
| Amir_Hossein_Arman | label | "Amir Hossein Arman" |
| Inbakavi | type | Person |
| Inbakavi | type | NamedIndividual |
| Inbakavi | label | "Inbakavi" |
| Inbakavi | altLabel | "Xavier Henric Leam" |
| actor | type | Occupation |
| actor | type | NamedIndividual |
| actor | label | "actor" |
| dramatist | type | Occupation |
| dramatist | type | NamedIndividual |
| dramatist | label | "dramatist" |
| model | type | Occupation |
| model | type | NamedIndividual |
| model | label | "model" |
| poet | type | Occupation |
| poet | type | NamedIndividual |
| poet | label | "poet" |
| singer | type | Occupation |
| singer | type | NamedIndividual |
| singer | label | "singer" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 7 |
| Extracted triples in scope | 27 |
| Ground-truth triples in scope | 5 |
| Union triples in scope | 27 |
| True positives (matched) | 5 |
| False positives (extracted-only) | 22 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.185185 |
| Recall | 1.000000 |
| F1 score | 0.312500 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
