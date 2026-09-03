# Triple matching report: 148

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Ang_Padrino | hasDirector | Fernando_Poe_Jr |
| Fernando_Poe_Jr | hasAwardReceived | National_Artist_of_the_Philippines |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 0**

| Subject | Predicate | Object |
|---|---|---|

## 2.2 Extracted-only triples

**Count: 13**

| Subject | Predicate | Object |
|---|---|---|
| Ang_Padrino | type | Film |
| Ang_Padrino | type | NamedIndividual |
| Ang_Padrino | label | "Ang Padrino" |
| Fernando_Poe_Jr | type | Person |
| Fernando_Poe_Jr | type | NamedIndividual |
| Fernando_Poe_Jr | label | "Fernando Poe Jr." |
| Fernando_Poe_Jr | altLabel | "Da King" |
| Fernando_Poe_Jr | altLabel | "FPJ" |
| Fernando_Poe_Jr | altLabel | "Ronald Allan Kelley Poe" |
| Fernando_Poe_Jr | altLabel | "Ronwaldo Reyes" |
| National_Artist_of_the_Philippines | type | Award |
| National_Artist_of_the_Philippines | type | NamedIndividual |
| National_Artist_of_the_Philippines | label | "National Artist of the Philippines for Film" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 3 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 15 |
| True positives (matched) | 2 |
| False positives (extracted-only) | 13 |
| False negatives (ground-truth-only) | 0 |
| Precision | 0.133333 |
| Recall | 1.000000 |
| F1 score | 0.235294 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
