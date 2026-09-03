# Triple matching report: 519

# 1. Matched triples

**Count: 2**

| Subject | Predicate | Object |
|---|---|---|
| Education_in_Chemistry | hasPublisher | Royal_Society_of_Chemistry |
| Royal_Society_of_Chemistry | hasCountry | United_Kingdom |

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
| Education_in_Chemistry | type | CreativeWork |
| Education_in_Chemistry | type | NamedIndividual |
| Education_in_Chemistry | label | "Education in Chemistry" |
| Royal_Society_of_Chemistry | type | Organization |
| Royal_Society_of_Chemistry | type | NamedIndividual |
| Royal_Society_of_Chemistry | label | "Royal Society of Chemistry" |
| United_Kingdom | type | Country |
| United_Kingdom | type | NamedIndividual |
| United_Kingdom | label | "United Kingdom" |

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
