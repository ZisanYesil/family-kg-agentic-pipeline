# Triple matching report: 92

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Angel_Square | hasDirector | Anne_Wheeler |

# 2. Unmatched triples

**Total unmatched count: 15**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Anne_Wheeler | hasAwardReceived | Officer_of_the_Order_of_Canada |

## 2.2 Extracted-only triples

**Count: 14**

| Subject | Predicate | Object |
|---|---|---|
| Angel_Square | type | Film |
| Angel_Square | type | NamedIndividual |
| Angel_Square | label | "Angel Square" |
| Anne_Wheeler | hasAwardReceived | gemini_award |
| Anne_Wheeler | hasAwardReceived | leo_award |
| Anne_Wheeler | type | Person |
| Anne_Wheeler | type | NamedIndividual |
| Anne_Wheeler | label | "Anne Wheeler" |
| gemini_award | type | Award |
| gemini_award | type | NamedIndividual |
| gemini_award | label | "Gemini Award" |
| leo_award | type | Award |
| leo_award | type | NamedIndividual |
| leo_award | label | "Leo Award" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 15 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 16 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 14 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.066667 |
| Recall | 0.500000 |
| F1 score | 0.117647 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
