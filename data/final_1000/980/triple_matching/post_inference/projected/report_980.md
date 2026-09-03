# Triple matching report: 980

# 1. Matched triples

**Count: 6**

| Subject | Predicate | Object |
|---|---|---|
| Alex_Lithgow | type | Agent |
| Alex_Lithgow | type | Person |
| Invercargill_March | hasComposer | Alex_Lithgow |
| Invercargill_March | hasCreator | Alex_Lithgow |
| Invercargill_March | type | Artifact |
| Invercargill_March | type | CreativeWork |

# 2. Unmatched triples

**Total unmatched count: 7**

## 2.1 Ground-truth-only triples

**Count: 3**

| Subject | Predicate | Object |
|---|---|---|
| Alex_Lithgow | hasCountry | Australian |
| Australian | type | Country |
| Australian | type | Place |

## 2.2 Extracted-only triples

**Count: 4**

| Subject | Predicate | Object |
|---|---|---|
| Alex_Lithgow | hasCountry | united_kingdom |
| Invercargill_March | type | MusicalWork |
| united_kingdom | type | Country |
| united_kingdom | type | Place |

# 3. Scope metrics

| Metric | Value |
|---|---:|
| Accepted entity pairs | 2 |
| Extracted triples in scope | 10 |
| Ground-truth triples in scope | 9 |
| Union triples in scope | 13 |
| True positives (matched) | 6 |
| False positives (extracted-only) | 4 |
| False negatives (ground-truth-only) | 3 |
| Precision | 0.600000 |
| Recall | 0.666667 |
| F1 score | 0.631579 |

_True negatives and accuracy are not reported because the universe of possible RDF triples is not defined._
