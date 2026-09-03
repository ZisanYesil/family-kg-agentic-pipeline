# Triple matching report: 980

# 1. Matched triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Invercargill_March | hasComposer | Alex_Lithgow |

# 2. Unmatched triples

**Total unmatched count: 13**

## 2.1 Ground-truth-only triples

**Count: 1**

| Subject | Predicate | Object |
|---|---|---|
| Alex_Lithgow | hasCountry | Australian |

## 2.2 Extracted-only triples

**Count: 12**

| Subject | Predicate | Object |
|---|---|---|
| Alex_Lithgow | hasCountry | united_kingdom |
| Alex_Lithgow | type | Person |
| Alex_Lithgow | type | NamedIndividual |
| Alex_Lithgow | label | "Alex Lithgow" |
| Alex_Lithgow | altLabel | "Alexander Frame Lithgow" |
| Invercargill_March | type | MusicalWork |
| Invercargill_March | type | NamedIndividual |
| Invercargill_March | label | "Invercargill March" |
| united_kingdom | type | Country |
| united_kingdom | type | NamedIndividual |
| united_kingdom | label | "United Kingdom" |
| united_kingdom | altLabel | "Scottish" |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 13 |
| Ground-truth triples in scope | 2 |
| Union triples in scope | 14 |
| True positives (matched) | 1 |
| False positives (extracted-only) | 12 |
| False negatives (ground-truth-only) | 1 |
| Precision | 0.076923 |
| Recall | 0.500000 |
| F1 score | 0.133333 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
